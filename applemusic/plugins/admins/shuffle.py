#
# Copyright (C) 2024 by TryToLiveAlone@Github, < https://github.com/TryToLiveAlone >.
#
# This file is part of < https://github.com/TryToLiveAlone/applemusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TryToLiveAlone/applemusic/blob/master/LICENSE >
#
# All rights reserved.
#

import random

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from applemusic import app # Rebranded import
from applemusic.misc import db # Rebranded import
from applemusic.utils.decorators import AdminRightsCheck # Rebranded import

# Commands
SHUFFLE_COMMAND = get_command("SHUFFLE_COMMAND")


@app.on_message(filters.command(SHUFFLE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["admin_21"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_22"])
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_22"])
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(_["admin_23"].format(message.from_user.first_name))
