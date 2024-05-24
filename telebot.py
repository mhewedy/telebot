import calendar
import logging
import os

import dateutil.parser
from telegram import Update
from telegram.ext import Application
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging = logging.getLogger(__name__)


class BotApp:

    def __init__(self):
        self.chat_id = os.getenv("CHAT_ID")
        bot_token = os.getenv("BOT_TOKEN")

        if self.chat_id is None or bot_token is None:
            raise ValueError("both CHAT_ID and BOT_TOKEN env vars should be set!")

        logging.info(f'CHAT_ID: {self.chat_id}')
        self.application = Application.builder().token(bot_token).build()
        self._cmds = []

    def command(self, name=None, desc=None, text=False, enabled=True, hidden=False):
        def wrapper(func):
            def wrapped_func(*args, **kwargs):
                logging.info(f"invoking command: {func.__name__}")

                (update, _) = args
                self.chat_id = update.edited_message.chat_id if update.edited_message else update.message.chat_id
                logging.info(f'setting chat_id to: {self.chat_id}')

                return func(*args, **kwargs)

            if enabled:
                if text:
                    self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, wrapped_func))
                else:
                    logging.info(f"declaring command: {name}")
                    if not hidden:
                        self._cmds.append((name, desc))
                    self.application.add_handler(CommandHandler(name, wrapped_func))
            return wrapped_func

        return wrapper

    def job(self, time=None, days=tuple(range(7)), interval=None, enabled=True):
        def wrapper(func):

            def wrapped_func(*args, **kwargs):
                logging.info(f"invoking job: {func.__name__}")
                new_args = args + (self.chat_id,)
                result = func(*new_args, **kwargs)
                return result

            if enabled:
                logging.info(
                    f'scheduling {func.__name__} at: {dateutil.parser.parse(time).time() if time else interval} '
                    + (f'on {[calendar.day_name[d] for d in days]}' if not interval else ''))
                wrapped_func.__name__ = f'w/{func.__name__}'
                if time:
                    self.application.job_queue.run_daily(wrapped_func, time=dateutil.parser.parse(time).time(),
                                                         days=days)
                else:
                    self.application.job_queue.run_repeating(wrapped_func, interval=interval)
            return wrapped_func

        return wrapper

    def help(self, name="help", desc="show help"):
        self._cmds.append((name, desc))
        self.application.add_handler(CommandHandler(name, self._help_command))
        self.application.add_handler(MessageHandler(filters.COMMAND, self._help_command))

    async def _help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("\n".join(f'/{name} -> {desc}' for (name, desc) in self._cmds))
