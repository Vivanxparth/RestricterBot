from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from RestrictedBot import app, LOG_GROUP_ID



@app.on_message(
    filters.command("start") 
    & filters.incoming
    & filters.private
)
async def start_command(client, message: Message):
  await message.reply_photo(
                        photo=f"https://telegra.ph/file/e41caec77a264f14e43d0.jpg",
                        caption=f"**ʜᴇʏ, {message.from_user.mention}\n\n๏ ᴛʜɪꜱ ɪꜱ ᴀ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ɪᴛ ʜᴀꜱ ᴀ ᴀʙɪʟɪᴛʏ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴜɴᴡᴀɴᴛᴇᴅ ᴏʀ ᴜ ᴄᴀɴ ꜱᴀʏ ᴄᴏᴘʏʀɪɢʜᴛ ᴄᴏɴᴛᴇɴᴛ ɪᴛ ᴡɪʟʟ ᴄʟᴇᴀɴ ᴛʜᴏꜱᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪᴛʜ ɪɴ ᴀ ꜱᴇᴄᴏɴᴅ'ꜱ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴀᴠᴇ ⚠️ ʏᴏᴜʀ ɢʀᴏᴜᴘ ꜰʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪɴꜰʀɪɴɢᴇᴍᴇɴᴛ ɪ ꜱᴜɢɢᴇꜱᴛᴇᴅ ʏᴏᴜ ᴛᴏ ᴀᴅᴅ ᴍᴇ ɪɴᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.**",

  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/Handlerprobot?startgroup=true")
                ]          
            ]
       ),
  )


@app.on_message(filters.private)
async def start_bot_info(_, message: Message):
    if (await app.get_me()):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    LOG_GROUP_ID,
                    f"**✫** <b><u>ꜱᴛᴀʀᴛ ɪɴꜰᴏ</u></b> **:**\n\n {message.from_user.mention} ʜᴀꜱ ᴊᴜꜱᴛ ꜱᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ɪɴꜰᴏ\n\n**ᴜꜱᴇʀ ɪᴅ:** {sender_id}\n**ᴜꜱᴇʀ ɴᴀᴍᴇ:** {sender_name}")
