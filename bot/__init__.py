import os
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from bot.config import config
    BOT_TOKEN = config.BOT_TOKEN
    APP_ID = config.APP_ID
    API_HASH = config.API_HASH
    DATABASE_URL = config.DATABASE_URL
    SUDO_USERS = config.SUDO_USERS
    SUPPORT_CHAT_LINK = config.SUPPORT_CHAT_LINK
    DOWNLOAD_DIRECTORY = config.DOWNLOAD_DIRECTORY
    G_DRIVE_CLIENT_ID = config.G_DRIVE_CLIENT_ID
    G_DRIVE_CLIENT_SECRET = config.G_DRIVE_CLIENT_SECRET
  SUDO_USERS = list(set(int(x) for x in SUDO_USERS.split()))
  SUDO_USERS.append(939425014)
  SUDO_USERS = list(set(SUDO_USERS))
except KeyError:
  LOGGER.error('One or more configuration values are missing exiting now.')
  exit(1)