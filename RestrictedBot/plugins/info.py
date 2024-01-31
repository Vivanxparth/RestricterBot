from pyrogram import Client, filters
from pyrogram.types import Message
from RestrictedBot import app, LOG_GROUP_ID


@app.on_message(filters.private)
async def start_bot_info(_, message: Message):
    if await is_on_off(LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    LOG_GROUP_ID,
                    f"**✫** <b><u>ꜱᴛᴀʀᴛ ɪɴꜰᴏ</u></b> **:**\n\n {message.from_user.mention} ʜᴀꜱ ᴊᴜꜱᴛ ꜱᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ɪɴꜰᴏ\n\n**ᴜꜱᴇʀ ɪᴅ:** {sender_id}\n**ᴜꜱᴇʀ ɴᴀᴍᴇ:** {sender_name}")
