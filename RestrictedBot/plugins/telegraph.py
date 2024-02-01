from pyrogram import Client, filters
import telegraph
from RestrictedBot import app

# Initialize the Telegraph client
telegraph_client = telegraph.Telegraph()

# handler for the /tl command
@app.on_message(filters.command("tl"))
def new_page_command(client, message):
    # Create a new page on Telegraph
    response = telegraph_client.create_page(
        title="Sample Page",
        content=["<p>Hello, this is a sample page created by the bot!</p>"]
    )
    telegraph_url = "https://graph.org/{}".format(response["path"])

    # Send the Telegraph URL as a reply
    message.reply_text(telegraph_url)
