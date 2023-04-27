from telethon import events
import handlers.client

client = handlers.client.client

@events.register(events.NewMessage(outgoing=True , pattern=r"\.hello"))
async def greeting(event):
    chat = await event.get_chat()
    # await client.send_message(chat , "Hello! How are you")
    await client.edit_message(event.message , "Hello ! How are you")
    # await event.reply("hello")