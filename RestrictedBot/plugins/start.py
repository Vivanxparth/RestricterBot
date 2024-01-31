from pyrogram import *
from pyrogram.types import *
from RestrictedBot import app

@app.on_message(filters.command("start"))
async def hello(app, message):
  await message.reply_photo(photo=f"https://telegra.ph/file/2938c50c7c6201bbd839e.jpg",
                              caption=f"Hey, {message.from_user.first_name}\n\n๏ This is a most powerful telegram bot it has a ability to delete unwanted or u can say copyright content it will clean those messages with in a second's if you want to save ⚠️ your group from copyright infringement I suggested you to add me into your group.",

  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ Add me to your Group", url=f"https://t.me/Handlerprobot?startgroup=true")
                ]          
            ]
       ),
  )
