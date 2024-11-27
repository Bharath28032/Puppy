from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your token
BOT_TOKEN = "8064025936:AAFdlFl0J0i9cXGCq7049X4P6ZkBDqABeqk"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Your bot is working!")

updater = Updater(token=BOT_TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
print("Bot is running...")
updater.idle()
