# Copyright (C) 2024 by TryToLiveAlone
# Released under the GNU v3.0 License Agreement

import asyncio
import threading

import uvloop
from flask import Flask
from pyrogram import Client, idle
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import (
    BotCommand,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

import config
from applemusic.logging import LOGGER

uvloop.install()

# Flask app initialize
app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is running"


def run():
    app.run(host="0.0.0.0", port=8000, debug=False)


class AppleMusicBot(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting AppleMusic Bot")
        super().__init__(
            "applemusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = get_me.first_name + " " + (get_me.last_name or "")
        self.mention = get_me.mention

        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="➕ Add Me to Group",
                        url=f"https://t.me/{self.username}?startgroup=true",
                    )
                ]
            ]
        )

        if config.LOG_GROUP_ID:
            try:
                await self.send_photo(
                    config.LOG_GROUP_ID,
                    photo=config.START_IMG_URL,
                    caption=(
                        f"🎵 **AppleMusic Bot Started!**\n\n"
                        f"👤 Name: {self.name}\n"
                        f"🆔 ID: `{self.id}`\n"
                        f"🔗 Username: @{self.username}\n"
                        f"💬 Thank you for using AppleMusic!"
                    ),
                    reply_markup=button,
                )
            except Exception as e:
                LOGGER(__name__).error(f"Failed to send startup message: {e}")
        else:
            LOGGER(__name__).warning("LOG_GROUP_ID not set. Skipping welcome message.")

        if config.SET_CMDS:
            try:
                await self.set_bot_commands(
                    commands=[
                        BotCommand("start", "Start the bot"),
                        BotCommand("help", "Help menu"),
                        BotCommand("ping", "Ping the bot"),
                    ],
                    scope=BotCommandScopeAllPrivateChats(),
                )
                await self.set_bot_commands(
                    commands=[
                        BotCommand("play", "Play requested song"),
                        BotCommand("stop", "Stop playback"),
                        BotCommand("pause", "Pause song"),
                        BotCommand("resume", "Resume song"),
                        BotCommand("queue", "View queue"),
                        BotCommand("skip", "Skip song"),
                        BotCommand("volume", "Adjust volume"),
                        BotCommand("lyrics", "Get song lyrics"),
                    ],
                    scope=BotCommandScopeAllGroupChats(),
                )
                await self.set_bot_commands(
                    commands=[
                        BotCommand("start", "Start bot"),
                        BotCommand("ping", "Ping test"),
                        BotCommand("help", "Help commands"),
                        BotCommand("vctag", "Voice chat tag all"),
                        BotCommand("stopvctag", "Stop VC tag"),
                        BotCommand("tagall", "Tag everyone"),
                        BotCommand("cancel", "Cancel tagging"),
                        BotCommand("settings", "View settings"),
                        BotCommand("reload", "Reload bot"),
                        BotCommand("play", "Play music"),
                        BotCommand("vplay", "Play video with music"),
                        BotCommand("end", "Clear queue"),
                        BotCommand("playlist", "Your playlist"),
                        BotCommand("stop", "Stop music"),
                        BotCommand("lyrics", "Fetch lyrics"),
                        BotCommand("song", "Download song"),
                        BotCommand("video", "Download video"),
                        BotCommand("gali", "Fun reply"),
                        BotCommand("shayri", "Get shayari"),
                        BotCommand("love", "Love shayari"),
                        BotCommand("sudolist", "View sudo list"),
                        BotCommand("owner", "Show owner"),
                        BotCommand("update", "Update bot"),
                        BotCommand("gstats", "Bot stats"),
                        BotCommand("repo", "Repository link"),
                    ],
                    scope=BotCommandScopeAllChatAdministrators(),
                )
            except Exception as e:
                LOGGER(__name__).error(f"Setting commands failed: {e}")

        if config.LOG_GROUP_ID:
            try:
                chat_member_info = await self.get_chat_member(
                    config.LOG_GROUP_ID, self.id
                )
                if chat_member_info.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error("Bot is not admin in LOG_GROUP_ID.")
            except Exception as e:
                LOGGER(__name__).error(f"LOG_GROUP_ID check failed: {e}")

        LOGGER(__name__).info(f"AppleMusic Bot started as {self.name}")


async def boot():
    bot = AppleMusicBot()
    await bot.start()
    await idle()


if __name__ == "__main__":
    LOGGER(__name__).info("Starting Flask server...")
    threading.Thread(target=run, daemon=True).start()

    LOGGER(__name__).info("Launching AppleMusicBot...")
    asyncio.run(boot())

    LOGGER(__name__).info("AppleMusicBot stopped.")
