from pyrogram import Client, filters
import os
from youtube_dl import YoutubeDL
from RestrictedBot import app
import yt_dlp


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'quiet': True,
}

# Define the download command
@app.on_message(filters.command("download") & filters.private)
async def download_song(client, message):
    # Get the query from the command
    query = message.text.split(None, 1)[1]

    # Download the song
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(query, download=True)
        song_file = f"{info_dict['title']}.mp3"
        await message.reply_document(open(song_file, "rb"))
        os.remove(song_file)
