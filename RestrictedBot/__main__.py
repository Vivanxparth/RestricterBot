from pyrogram import Client, filters, idle
import re
import asyncio
import os
import importlib
from RestrictedBot import app, LOGGER
from RestrictedBot.plugins import ALL_MODULES

# Pyrogram client
app = Client(
             "my_bot", 
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
