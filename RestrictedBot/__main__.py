from pyrogram import Client, filters, idle
import re
import asyncio
from os import getenv
import os
from pyrogram import __version__ as pyr
import importlib
from RestrictedBot import app
from RestrictedBot.plugins import ALL_MODULES

#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Pyrogram client
app = Client(
             name="RestrictedBot", 
             api_id=API_ID, 
             api_hash=API_HASH, 
             bot_token=BOT_TOKEN,
)

async def app_boot():
    try:
        await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("RestrictedBot.plugins" + all_module)
    LOGGER("RestrictedBot.plugins").info("Successfully Imported Modules...")
    LOGGER("RestrictedBot").info(
        "Bot Started Successfully"
    )
    await idle()
    await app.stop()
    LOGGER("RestrictedBot").info("Stopping Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
