from telethon import TelegramClient, events
from telethon.tl.patched import Message
from telethon.tl.types import Chat, User
from config import API_ID, API_HASH, WORDLIST, BOTNICK

client = TelegramClient("notify-on-untagged", int(API_ID), API_HASH)
client.parse_mode = "markdown"


@client.on(events.NewMessage)
async def check_message(event):
    message: Message = event.message
    c: Chat = await message.get_chat()
    sender: User = await message.get_sender()
    try:
        name = sender.username or sender.first_name
    except AttributeError:
        name = sender.username
    found = len(list(filter(lambda x: x in message.message.lower(), WORDLIST))) > 0
    if found and (message.mentioned is False or message.mentioned is None):
        to_send = f"[{name}](tg://user?id={message.from_id.user_id}) "
        to_send += f"tagged you in [{c.id}](https://t.me/c/{c.id}/{message.id})"
        await client.send_message(BOTNICK, to_send)
