import os

from telegram import Update
from telegram.ext import ContextTypes

from telebot import BotApp

os.environ["CHAT_ID"] = "<put chat id>"
os.environ["BOT_TOKEN"] = "<put bot token>"

bot = BotApp()


@bot.command(name="ping", desc="test the bot")
async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Pong!")


@bot.job(time="08:00")
async def send_lunch_headsup(context: ContextTypes.DEFAULT_TYPE, chat_id):
    await context.bot.send_message(chat_id, text="hello from timer")


@bot.job(interval=5)
async def send_lunch_headsup(context: ContextTypes.DEFAULT_TYPE, chat_id):
    await context.bot.send_message(chat_id, text="hello from interval")


if __name__ == '__main__':
    bot.help()
    bot.application.run_polling(allowed_updates=Update.ALL_TYPES)
