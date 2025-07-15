# Copyright (C) 2024 by TryToLiveAlone
# This project is based on VIP-MUSIC but now adapted and renamed by @TryToLiveAlone
# Released under the MIT License

import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS

from applemusic import HELPABLE, LOGGER, app, userbot
from applemusic.core.call import CallManager
from applemusic.plugins import ALL_MODULES
from applemusic.utils.database import get_banned_users, get_gbanned


async def init():
    # Ensure at least one assistant session string is defined
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("applemusic").error(
            "No assistant session strings defined. Exiting."
        )
        return

    if not config.SPOTIFY_CLIENT_ID or not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("applemusic").warning(
            "No Spotify credentials found. Spotify queries will not work."
        )

    # Load banned users from database
    try:
        gbanned_users = await get_gbanned()
        BANNED_USERS.update(gbanned_users)

        banned_users = await get_banned_users()
        BANNED_USERS.update(banned_users)
    except Exception:
        pass

    # Start the bot
    await app.start()

    # Dynamically load all plugin modules
    for module_name in ALL_MODULES:
        imported_module = importlib.import_module(module_name)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module

    LOGGER("applemusic.plugins").info("Successfully imported all modules.")

    # Start the userbot and voice call client
    await userbot.start()
    await CallManager.start()
    await CallManager.decorators()

    LOGGER("applemusic").info("AppleMusic Bot started successfully 🕊️")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("applemusic").info("AppleMusic Bot is shutting down. Goodbye!")
  
