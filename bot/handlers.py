from telegram import Update
from telegram.ext import CallbackContext


def ban_command(update: Update, context: CallbackContext):
    update.message.reply_text('ban ishldi.')
