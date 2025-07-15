# Copyright (C) 2024 by TryToLiveAlone
# Cleaned and adapted from original VIP-MUSIC project
# Released under the MIT License

import logging
from logging.handlers import RotatingFileHandler

from config import LOG_FILE_NAME

# Configure base logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=5_000_000, backupCount=10),
        logging.StreamHandler(),
    ],
)

# Silence noisy logs from common libraries
for noisy_logger in ["apscheduler", "pyrogram", "pytgcalls", "pymongo", "ntgcalls", "httpx"]:
    logging.getLogger(noisy_logger).setLevel(logging.ERROR)

# Logger wrapper function
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
