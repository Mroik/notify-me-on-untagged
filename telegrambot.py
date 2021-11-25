import logging

from telegram.ext import Updater, Dispatcher, CallbackContext, MessageHandler
from telegram.ext.filters import Filters
from telegram import Bot, Update

from config import BOT_TOKEN, USER_ID, GROUP_ID


LOG = logging.getLogger(__name__)
updater = Updater(token=BOT_TOKEN)
disp: Dispatcher = updater.dispatcher
bot: Bot = updater.bot


def handle_msg_rec(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != int(USER_ID):
        return
    update.message.forward(int(GROUP_ID))
    LOG.info(f"Message from {update.message.from_user.id} was forwarded to {GROUP_ID}")


disp.add_handler(MessageHandler(Filters.update, callback=handle_msg_rec))
