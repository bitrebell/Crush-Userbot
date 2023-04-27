from telethon import events
import handlers.client
import os

client = handlers.client.client


@events.register(events.NewMessage(outgoing=True , pattern=r"\.alive"))
async def alive(event):
    chat = await event.get_chat()
    photo = await client.download_profile_photo('me')
    me = await client.get_me()
    await client.delete_messages(chat , event.message)
    await client.send_file(chat , file = photo , 
                           caption = 
                           "be better man i always ready to do be positive\n"
                           "Owner = [CRUSH](https://t.me/{})\n"
                           "Channel = [Support]({})\n".format(me.username , 'https://t.me/sudogrouppp')
                           )
    os.remove(photo)