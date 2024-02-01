import requests
from RestrictedBot import app as bot
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@bot.on_message(filters.command("ask"))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "❍ Example ➛ /ask ᴡʜᴇʀᴇ ɪs ᴛᴀᴊᴍᴀʜᴀʟ ?")
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://mukesh-api.vercel.app/chatgpt/{a}') 
            x=response.json()["results"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"❍ {x}\n\n❍ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ ๛ᴀ ᴠ ɪ s ʜ ᴀ ༗ ", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
