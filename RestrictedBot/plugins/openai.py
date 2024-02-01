from pyrogram import Client, filters
import openai
from RestrictedBot import app


# Configure the OpenAI API with your API key
openai.api_key = "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"

# Define a handler for incoming messages
@app.on_message(filters.command("ask") & filters.group & ~filters.me)
async def chat_gpt(client, message):
    await message.reply_text(f"**Usage: /ask**")
    # Get the user's message
    user_message = message.text

    # Use OpenAI's GPT-3 API to generate a response
    response = openai.Completion.create(
      engine="davinci", 
      prompt=user_message, 
      max_tokens=100
    )

    # Send the response back to the user
    message.reply_text(response["choices"][0]["text"])
