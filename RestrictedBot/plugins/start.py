import asyncio
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton
from RestrictedBot import app

@app.on_message(filters.command("start") & filters.private)
async def hello(app, message):
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
       )
  )
