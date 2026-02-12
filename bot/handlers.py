from telegram import Update, ChatMember, ChatPermissions
from telegram.ext import CallbackContext


def ban_command(update: Update, context: CallbackContext):
    chat_member = context.bot.get_chat_member(
        chat_id="@testeaknjdfkjasndkjfs", user_id=update.effective_user.id
    )
    if not chat_member:
        context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.message.message_id
        )
        return

    if chat_member.status not in (ChatMember.ADMINISTRATOR, ChatMember.CREATOR):
        context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.message.message_id
        )
        return

    if update.message.reply_to_message is None:
        context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.message.message_id
        )
        return

    reply_to_message = update.message.reply_to_message
    from_user = reply_to_message.from_user

    chat_member = context.bot.get_chat_member(
        chat_id="@testeaknjdfkjasndkjfs", user_id=from_user.id
    )

    if not chat_member:
        context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.message.message_id
        )
        return

    if chat_member.status in (ChatMember.ADMINISTRATOR, ChatMember.CREATOR):
        context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.message.message_id
        )
        return

    context.bot.restrict_chat_member(
        chat_id=update.effective_chat.id,
        user_id=from_user.id,
        permissions=ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False,
        ),
    )

    context.bot.delete_message(
        chat_id=update.effective_chat.id, message_id=reply_to_message.message_id
    )
    update.message.reply_text(f"{from_user.first_name}-user ban qilindi")
