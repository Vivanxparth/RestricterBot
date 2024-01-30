from pyrogram import filters
from pyrogram.types import Message

from RestrictedBot import app


@app.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(_, message: Message):
    await message.reply_text(
        text=f"Hey, {message.from_user.first_name},\n\n๏ This is  {app.mention},\nand my work is to restrict usee to sending copyright messages in public groups."
    )
    
