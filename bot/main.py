from telegram.ext import (
    Updater,
    CommandHandler,
)

from bot.config import settings
from bot.handlers import (
    ban_command,
)


def main():
    updater = Updater(settings.BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('ban', ban_command))

    updater.start_polling()
    updater.idle()
