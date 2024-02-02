import asyncio
import os
from os import getenv
import logging
from pyrogram import Client


logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", ""))
OWNER_ID = int(os.getenv("OWNER_ID", ""))
               
class app(Client):
    def __init__(self):
        super().__init__(
            name="RestrictBot",
            api_id=API_ID,
            api_hash=API_HASH,           
            bot_token=BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

    async def stop(self):
        await super().stop()


app = app()
