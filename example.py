import os

from telegram import Update
from telegram.ext import ContextTypes

from telebot import BotApp

os.environ["CHAT_ID"] = "<put chat id>"
os.environ["BOT_TOKEN"] = "<put bot token>"

bot = BotApp()


@bot.command(text=True)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


@bot.command(name="ping", desc="test the bot")
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Pong!")


@bot.job(time="08:00", enabled=False)
async def hell_timer(context: ContextTypes.DEFAULT_TYPE, chat_id):
    await context.bot.send_message(chat_id, text="hello from timer")


@bot.job(interval=5, enabled=True)
async def hello_interval(context: ContextTypes.DEFAULT_TYPE, chat_id):
    await context.bot.send_message(chat_id, text="hello from interval")


if __name__ == '__main__':
    bot.help()
    bot.application.run_polling(allowed_updates=Update.ALL_TYPES)
