from RestrictedBot import app
from pyrogram.types import Message
from pyrogram import Client, filters

@app.on_message(
    filters.command("ping")
    & filters.group
)  
async def ping_command(client, message: Message):
    response = await message.reply_text(f"Pinging 🏓",
    )
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(f"˜”*°•.˜”*°• ριηg\n\n˜”*°•.˜”*°• ρσηg", resp
    )
