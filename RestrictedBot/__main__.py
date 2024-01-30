import asyncio
import importlib
from pyrogram import idle
from RestrictedBot import LOGGER, app
from RestrictedBot.plugins import ALL_MODULES


async def app_boot():
    try:
        await app.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("RestrictedBot.plugins" + all_module)

    LOGGER.info(f"@{app.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping Bot...")
