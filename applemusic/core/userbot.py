#
# Copyright (C) 2024 by TryToLiveAlone@Github, < https://github.com/TryToLiveAlone >.
#
# This file is part of < https://github.com/TryToLiveAlone/applemusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TryToLiveAlone/applemusic/blob/master/LICENSE >
#
# All rights reserved.
#


from typing import Callable, Optional

import pyrogram
from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []
clients = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            "applemusicString1",  # Rebranded client name
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
        )

        self.two = Client(
            "applemusicString2",  # Rebranded client name
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
        )

        self.three = Client(
            "applemusicString3",  # Rebranded client name
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
        )

        self.four = Client(
            "applemusicString4",  # Rebranded client name
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
        )

        self.five = Client(
            "applemusicString5",  # Rebranded client name
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant Clients")
        if config.STRING1:
            await self.one.start()
            try:
                # Updated channels to join
                await self.one.join_chat("TeleAPI_services")
                await self.one.join_chat("TeleFilx_Service")
            except:
                pass
            assistants.append(1)
            clients.append(self.one)
            try:
                await self.one.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).info(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            self.one.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = get_me.first_name + " " + get_me.last_name
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")
        if config.STRING2:
            await self.two.start()
            try:
                # Updated channels to join
                await self.two.join_chat("TeleAPI_services")
                await self.two.join_chat("TeleFilx_Service")
            except:
                pass
            assistants.append(2)
            clients.append(self.two)
            try:
                await self.two.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                # sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            self.two.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = get_me.first_name + " " + get_me.last_name
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")
        if config.STRING3:
            await self.three.start()
            try:
                # Updated channels to join
                await self.three.join_chat("TeleAPI_services")
                await self.three.join_chat("TeleFilx_Service")
            except:
                pass
            assistants.append(3)
            clients.append(self.three)
            try:
                await self.three.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                # sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            self.three.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = get_me.first_name + " " + get_me.last_name
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")
        if config.STRING4:
            await self.four.start()
            try:
                # Updated channels to join
                await self.four.join_chat("TeleAPI_services")
                await self.four.join_chat("TeleFilx_Service")
            except:
                pass
            assistants.append(4)
            clients.append(self.four)
            try:
                await self.four.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                # sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            self.four.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = get_me.first_name + " " + get_me.last_name
            else:
                self.four.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")
        if config.STRING5:
            await self.five.start()
            try:
                # Updated channels to join
                await self.five.join_chat("TeleAPI_services")
                await self.five.join_chat("TeleFilx_Service")
            except:
                pass
            assistants.append(5)
            clients.append(self.five)
            try:
                await self.five.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                # sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            self.five.mention = get_me.mention
            assistantids.append(get_me.id)


def on_cmd(
    filters: Optional[pyrogram.filters.Filter] = None, group: int = 0
) -> Callable:
    def decorator(func: Callable) -> Callable:
        for client in clients:
            client.add_handler(pyrogram.handlers.MessageHandler(func, filters), group)
        return func

    return decorator
