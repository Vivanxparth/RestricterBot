from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from RestrictedBot import app

pytgcalls = PyTgCalls(app)

# Handle the play command
@app.on_message(filters.command("play") & filters.private)
async def play(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    # Check if the user is in a voice chat
    if "voice" in message.chat.type:
        # Stream a file to the group voice chat
        path_to_audio_file = "path_to_audio_file.mp3"  # Replace with the actual path to your audio file
        await pytgcalls.join_group_call(
            chat_id,
            path_to_audio_file,
            enable_logs=True
        )
    else:
        await message.reply_text("You must join a voice chat to play music.")

