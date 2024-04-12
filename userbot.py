from telethon import TelegramClient, events
from telethon.tl.patched import Message
from telethon.tl.types import Chat
from config import API_ID, API_HASH, WORDLIST, BOTNICK

client = TelegramClient("notify-on-untagged", int(API_ID), API_HASH)
client.parse_mode = "markdown"


@client.on(events.NewMessage)
async def check_message(event):
    message: Message = event.message
    c: Chat = await message.get_chat()
    found = len(list(filter(lambda x: x in message.message.lower(), WORDLIST))) > 0
    if found and not message.mentioned:
        print(f"[{message.chat_id}](https://t.me/c/{message.chat_id}/{message.id})")
        to_send = f"[{message.from_id.user_id}](tg://user?id={message.from_id.user_id}) "
        to_send += f"tagged you in [{c.id}](https://t.me/c/{c.id}/{message.id})"
        await client.send_message(BOTNICK, to_send)
