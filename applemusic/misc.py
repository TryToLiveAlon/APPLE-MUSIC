# Copyright (C) 2024 by TryToLiveAlone
# Released under the MIT License

import socket
import time

import heroku3
from pyrogram import filters

import config
from applemusic.core.mongo import pymongodb
from applemusic.logging import LOGGER

SUDOERS = filters.user()
HAPP = None
_boot_ = time.time()

def is_heroku():
    return "heroku" in socket.getfqdn()

XCB = [
    "/", "@", ".", "com", ":", "git", "heroku", "push",
    str(config.HEROKU_API_KEY),
    "https", str(config.HEROKU_APP_NAME), "HEAD", "main",
]

def dbb():
    global db, clonedb
    db = {}
    clonedb = {}
    LOGGER(__name__).info("Database Initialized.")

def sudo():
    global SUDOERS
    OWNER = config.OWNER_ID

    if config.MONGO_DB_URI is None:
        for user_id in OWNER:
            SUDOERS.add(user_id)
    else:
        sudoersdb = pymongodb.sudoers
        sudoers = sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]

        for user_id in OWNER:
            SUDOERS.add(user_id)
            if user_id not in sudoers:
                sudoers.append(user_id)
                sudoersdb.update_one(
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers}},
                    upsert=True,
                )

        for x in sudoers:
            SUDOERS.add(x)

    LOGGER(__name__).info("Sudoers Loaded.")

def heroku():
    global HAPP
    if is_heroku():
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info("Heroku App Configured")
            except BaseException:
                LOGGER(__name__).warning(
                    "Please check your Heroku API Key and App name configuration."
)
