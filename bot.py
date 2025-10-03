import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")  # your bot token will be stored in Railway

def start(update, context):
    update.message.reply_text("Hello! I am your subscription bot 😊")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
