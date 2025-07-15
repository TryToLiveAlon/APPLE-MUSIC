#
# Copyright (C) 2024 by TryToLiveAlone@Github, < https://github.com/TryToLiveAlone >.
#
# This file is part of < https://github.com/TryToLiveAlone/applemusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TryToLiveAlone/applemusic/blob/master/LICENSE >
#
# All rights reserved.
#

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import config

from ..logging import LOGGER

TEMP_MONGODB = "mongodb+srv://AppleMuisc:AppleMuisc@cluster0.kunkxjv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning(
        "𝐍o 𝐌ONGO 𝐃B 𝐔RL 𝐅ound.. 𝐘our 𝐁ot 𝐖ill 𝐖ork 𝐎n 𝐀pple𝐌usic 𝐃atabase" # Changed "VIP MUSIC" to "AppleMusic"
    )
    temp_client = Client(
        "applemusic", # Changed "VIPMUSIC" to "applemusic"
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.applemusic # Changed ".VIPMUSIC" to ".applemusic"
    pymongodb = _mongo_sync_.applemusic # Changed ".VIPMUSIC" to ".applemusic"
