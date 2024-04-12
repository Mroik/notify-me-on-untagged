import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from config import BOT_TOKEN, CHANNEL_ID, USER_ID


async def relay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != int(USER_ID):
        return
    await update.message.forward(int(CHANNEL_ID))
    LOG.info(f"Message from {update.message.from_user.name} was forwarded to {CHANNEL_ID}")
    await update.message.delete()

LOG = logging.getLogger(__name__)
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, relay))
