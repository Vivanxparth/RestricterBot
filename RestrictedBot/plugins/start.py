import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from RestrictedBot import app, LOG_GROUP_ID


@app.on_message(
    filters.command("start", prefixes="/")
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
                        "✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/Handlerprobot?startgroup=true"),
                ],         
            ]
       )
  )
    
  await client.send_message(
                LOG_GROUP_ID,
                f"**BOT INFO**: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"**BOT INFO** :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
