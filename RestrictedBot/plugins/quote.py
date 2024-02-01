from pyrogram import Client, filters
import requests
from RestrictedBot import app
from pyrogram.types import Message

# Define the quote command
@app.on_message(filters.command("quote") & filters.group)
async def send_quote(client, message: Message):
    response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
    if response.status_code == 200:
        quote_data = response.json()
        quote_text = quote_data["quoteText"]
        quote_author = quote_data["quoteAuthor"] if quote_data.get("quoteAuthor") else "Unknown"

        quote_message = f"\"{quote_text}\"\n- {quote_author}"
        await message.reply_text(quote_message)
    else:
        await message.reply_text("Failed to fetch a quote at the moment. Please try again later.")

