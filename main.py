from telethon import TelegramClient , events , client
import os
from html_telegraph_poster.upload_images import upload_image
import handlers.client , handlers.hello , handlers.alive

client = handlers.client.client 


# hello command 
with client as aadil:
    aadil.add_event_handler(handlers.hello.greeting)

# bio command 
@client.on(events.NewMessage(outgoing=True , pattern=r"\.bio"))
async def aboutme(event):
    chat = await event.get_chat()
    await client.edit_message(event.message , "Hey My Name Is Aadil Shiekh. I am a student and a python developer, Nice to meet you")

# alive command
with client as aadil:
    aadil.add_event_handler(handlers.alive.alive)


#Telegraph Upload
# @client.on(events.NewMessage(outgoing=True , pattern=r"\.tu"))
# async def TelegraphUpload(event):
#     chat = await event.get_chat()
#     replied = await event.get_reply_message()
#     image = await replied.download_media()
#     x = upload_image(image) 

client.start()
client.run_until_disconnected()
