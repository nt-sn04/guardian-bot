from telegram.ext import BaseFilter
from telegram import Update, Chat


class CustomFilters:
    class IsGroup(BaseFilter):
        def __call__(self, update: Update):
            if update.message is None:
                return False

            return update.message.chat.type in (Chat.GROUP, Chat.SUPERGROUP)

    is_group = IsGroup()
