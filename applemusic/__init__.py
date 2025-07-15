import json
import os

# Core system imports (renamed from VIP to Apple)
from applemusic.core.bot import Bot
from applemusic.core.dir import dirr
from applemusic.core.git import git
from applemusic.core.userbot import Userbot
from applemusic.core.youtube import youtube_init

# Misc utilities
from applemusic.misc import dbb, heroku, sudo

# Logging
from .logging import LOGGER

# Run initialization steps
dirr()        # Prepare necessary directories
git()         # Fetch latest git info if needed
dbb()         # Connect to MongoDB
heroku()      # Initialize Heroku env if available
sudo()        # Load sudo users
youtube_init() # YouTube utilities init

# Initialize bot and userbot
app = Bot()
userbot = Userbot()

# Platform APIs
from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

# Help command registry
HELPABLE = {}
