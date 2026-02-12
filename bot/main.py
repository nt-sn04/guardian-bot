from telegram.ext import (
    Updater,
    CommandHandler,
)

from bot.config import settings
from bot.handlers import (
    ban_command,
)
from bot.filters import CustomFilters


def main():
    updater = Updater(settings.BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(
        handler=CommandHandler(
            command="ban", callback=ban_command, filters=CustomFilters.is_group
        )
    )

    updater.start_polling()
    updater.idle()
