# This module can help you to prevent your group from copyright content. this can delete messages which contains more than 50 words so say fu*k off to the copyright content.
# Pyrogram 2.0 supported module.
# MIT-License copyright own by kopelor 2024-25.
# Delete all admin non admin messages which are blocked.

import re
from pyrogram import Client, filters
from RestrictedBot import app
from pyrogram.types import Message


# Define the maximum length for messages
max_message_length = 50  # Adjust the maximum length as needed


# Event handler to delete long messages
@app.on_message(filters.text)
async def delete_long_messages(client, message):
    if len(message.text) > max_message_length:
        await client.delete_messages(message.chat.id, message.id)


# Delete edited messages
@app.on_edited_message(filters.group)
async def delete_edited_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with files
@app.on_message(filters.document)
async def delete_file_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)



# Regular expression pattern to match bio links
bio_link_pattern = re.compile(r'(http|https)://[^\s]+')


# Delete messages with bio links
@app.on_message(filters.text & filters.private)
async def delete_bio_link_messages(client, message):
    if bio_link_pattern.search(message.text):
        await client.delete_messages(message.chat.id, message.id)


# Delete messages with photo
@app.on_message(filters.photo & filters.group)
async def delete_photo_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with video
@app.on_message(filters.video)
async def delete_video_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with sticker
@app.on_message(filters.sticker)
async def delete_sticker_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete channel messages
@app.on_message(filters.channel)
async def delete_channel_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with audio
@app.on_message(filters.audio)
async def delete_audio_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with forwarded 
@app.on_message(filters.forwarded)
async def delete_forwarded_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with animation
@app.on_message(filters.animation)
async def delete_file_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)



# Delete messages with voice note
@app.on_message(filters.voice)
async def delete_voice_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with video note
@app.on_message(filters.video_note)
async def delete_video_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)



# Regular expression pattern to match links
link_pattern = re.compile(r'(http[s]?:\/\/)?[^\s(["<,>.]+?\.[^\s[">,<.]+')

# Delete messages with links
@app.on_message(filters.text & filters.group)
async def delete_link_messages(client, message):
    if link_pattern.search(message.text):
        await client.delete_messages(message.chat.id, message.id)
