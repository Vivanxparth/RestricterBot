from RestrictedBot import app
from pyrogram.types import Message
from pyrogram import *

@app.on_message(
    filters.command("ping")
    & filters.group
)
async def ping_command(client, message: Message):
    await message.reply_text(f"˜”*°•.˜”*°• ριηg\n\n˜”*°•.˜”*°• ρσηg" 
    )
    
