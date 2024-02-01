from pyrogram import Client, filters
import telegraph


# Initialize the Telegraph client
telegraph_client = telegraph.Telegraph()

# Define a handler for the /tl command
@app.on_message(filters.command("tl"))
async def make_link_command(client, message):
    # Extract the content from the user's message
    content = message.text.split("/tl", 1)[1].strip()

    # Create a new page on Telegraph
    response = telegraph_client.create_page(
        title="Telegram Bot Generated Page",
        content=[content]
    )
    telegraph_url = "https://telegra.ph/{}".format(response["path"])

    # Send the Telegraph URL as a reply
    await message.reply_text(f"Here is your Telegraph link: {telegraph_url}")
