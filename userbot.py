import re
import logging

from telethon import TelegramClient, events
from telethon.tl.types import PeerUser

from config import API_ID, API_HASH, WORDLIST, BOT_ID


LOG = logging.getLogger(__name__)
client = TelegramClient("notify me on untagged", API_ID, API_HASH)
client.parse_mode = "markdown"


@client.on(events.NewMessage())
async def handler(event: events.NewMessage.Event):
    me = await client.get_me()
    from_ = event.message.from_id
    chan = event.message.peer_id
    message = event.message

    if isinstance(event.message.peer_id, PeerUser):
        return
    if int(BOT_ID) == from_.user_id:
        return
    if from_.user_id == me.id:
        return
    if message.message == "" or message.message is None:
        return
    if message.mentioned:
        return
    for word in WORDLIST:
        if f" {word.upper()} " in message.message.upper()\
                or message.message.upper().startswith(f"{word.upper()} ")\
                or message.message.upper().endswith(f" {word.upper()}"):
            msg = f"[{from_.user_id}](tg://user?id={from_.user_id}) tagged you in"
            msg += f" [{chan.channel_id}](https://t.me/c/{chan.channel_id}/{str(message.id)}):\n"
            found = re.search(f"{word.upper()}", message.message.upper())
            if found is None:
                msg += f"{message.message}"
            else:
                msg += f"{message.message[:found.start()]}__"\
                       f"{message.message[found.start():found.end()]}__"\
                       f"{message.message[found.end():]}"
            await client.send_message(await client.get_input_entity(int(BOT_ID)), msg)
            LOG.info(f"Message from {from_.user_id} was sent to BOT {BOT_ID}")
            return
