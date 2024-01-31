from pyrogram import Client, filters
from io import BytesIO
from PIL import Image
import torch
import torchvision.transforms as transforms
from RestrictedBot import app, OWNER_ID

# Load a pre-trained Super-Resolution model (for example EDSR)
model = torch.hub.load('zhanghang1989/EDSR-PyTorch', 'edsr_x2', pretrained=True).eval()


# Define the upscale command
@app.on_message(filters.command("upscale") & filters.photo)
async def upscale_image(client, message):
    # Only the user can use the bot
    if message.from_user.id == OWNER_ID:
        # Download the photo
        photo_path = await message.download()
        photo = Image.open(photo_path)

        # Convert the photo to YCbCr format
        ycbcr = photo.convert('YCbCr')
        y, cb, cr = ycbcr.split()

        # Apply the Super-Resolution model
        input = transforms.ToTensor()(y).view(1, -1, y.size[1], y.size[0])
        out = model(input).data.squeeze().clamp(0, 1)
        out_img_y = torch.cat((out, cb.resize(out.size, Image.BICUBIC), cr.resize(out.size, Image.BICUBIC)), 0)

        # Convert back to RGB
        out_img = transforms.ToPILImage()(out_img_y)

        # Save the upscaled image to memory
        buffered = BytesIO()
        out_img.save(buffered, format="JPEG")
        buffered.seek(0)

        # Send the upscaled photo
        await app.send_photo(message.chat.id, photo=buffered)

        # Cleanup
        out_img.close()
        photo.close()
    else:
        await message.reply_text("You are not authorized to use this command.")
