import asyncio
from pyrogram import Client, filters
from RestrictedBot import app

# Define the broadcast command
@app.on_message(filters.command("broadcast") & filters.group)
async def broadcast(client, message):
    # Check if the user is the bot owner
    if message.from_user.id == your_user_id:
        # Split the command into message and media
        try:
            command, *text = message.text.split(maxsplit=1)
            text = text[0]
            if message.reply_to_message and message.reply_to_message.media:
                # Broadcast message with media
                media = message.reply_to_message
                async for dialog in app.iter_dialogs():
                    if dialog.chat.type in ("group", "supergroup", "channel"):
                        await app.send_media(dialog.chat.id, media=media, caption=text)
                await message.reply_text("Broadcast completed successfully!")
            else:
                # Broadcast message without media
                async for dialog in app.iter_dialogs():
                    if dialog.chat.type in ("group", "supergroup", "channel"):
                        await app.send_message(dialog.chat.id, text)
                await message.reply_text("Broadcast completed successfully!")
        except Exception as e:
            await message.reply_text(f"An error occurred: {e}")
    else:
        await message.reply_text("You are not authorized to use this command.")
