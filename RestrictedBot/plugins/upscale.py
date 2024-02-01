from pyrogram import Client, filters
import requests
import io
from RestrictedBot import app


# Define a handler for the /upscale command
@app.on_message(filters.command("upscale"))
def upscale_command(client, message):
    # Get the photo file ID from the message
    photo = message.photo[-1] if message.photo else (message.document if message.document.mime_type.startswith("image") else None)

    if photo:
        # Download the photo
        file_path = client.download_media(photo, file_name="photo.jpg")

        # Upscale the image using Let's Enhance API
        url = "https://api.letsenhance.io/v2/upscale"
        files = {'image': open(file_path, 'rb')}
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            # Send the upscaled image as a reply
            message.reply_photo(io.BytesIO(response.content))
        else:
            message.reply_text("Failed to process the image. Please try again.")
    else:
        message.reply_text("Please provide an image to upscale.")
