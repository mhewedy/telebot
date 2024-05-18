# Telebot

Telegram bot library abstraction on top
of [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Features

Help you to get started quickly by providing decorators `@command` and `@job`

## Install
```bash
pip install --upgrade --force-reinstall git+https://github.com/mhewedy/telebot
```

### Example:

```python

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

```

see example.py for the whole running example
