from pyrogram import Client, filters
from RestrictedBot import app, OWNER_ID


# Define the broadcast command
@app.on_message(filters.command("broadcast") & filters.group)
async def broadcast_message(client, message):
    # Check if the sender is the bot owner
    if message.from_user.id == OWNER_ID:
        # Get the message to broadcast
        text = message.text.split(maxsplit=1)[1]
        
        # Send the broadcast message to each conversation
        async for dialog in app.iter_dialogs():
            if dialog.chat.type in ("group", "supergroup", "channel"):
                await app.send_message(dialog.chat.id, text)
        
        # Reply to the sender
        await message.reply_text("Broadcast completed successfully!")
    else:
        # If the sender is not authorized, inform them
        await message.reply_text("You are not authorized to use this command.")


# Generate the private chat link
private_chat_link = f"https://t.me/handlerprobot?start=private"

print("Here's the private chat link:")
print(private_chat_link)
