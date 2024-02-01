from telegraph import upload_file
from pyrogram import filters
from RestrictedBot import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command("tl") & filters.incoming & filters.group)
def telegraph(client, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("Please Wait!")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x
            
        i.edit(f'`{url}`')
