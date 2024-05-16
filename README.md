# Telebot

Telegram bot library abstraction on top
of [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Features

it helps you getting started quickly by providing to decorators `@command` and `@job`

### Example:

```python
@bot.command(name="ping", desc="test the bot")
async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Pong!")


@bot.job(time="08:00")
async def send_lunch_headsup(context: ContextTypes.DEFAULT_TYPE, chat_id):
    await context.bot.send_message(chat_id, text="hello from timer")


@bot.job(interval=5)
async def send_lunch_headsup(context: ContextTypes.DEFAULT_TYPE, chat_id):
    await context.bot.send_message(chat_id, text="hello from interval")
```

see example.py for the whole running example