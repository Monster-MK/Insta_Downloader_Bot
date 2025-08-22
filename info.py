import os
import re
from dotenv import load_dotenv

# Load from config.env (local testing)
load_dotenv("config.env")

# Regex for ID validation
id_pattern = re.compile(r'^-?\d+$')

# ===============================
# Telegram Bot Settings
# ===============================
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
OWNER_ID = int(os.getenv("OWNER_ID"))

# ===============================
# Bot Pics
# ===============================
PICS = (os.getenv("PICS", "https://files.catbox.moe/7ugjlq.jpg")).split()

# ===============================
# Channels
# ===============================
INSTA_CHANNEL = int(os.getenv("INSTA_CHANNEL"))     # For storing Instagram media
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))         # For errors, status updates

# ===============================
# Database
# ===============================
MONGO_DB_URI = os.getenv("MONGO_DB_URI")            # MongoDB connection string
DB_NAME = os.getenv("DB_NAME", "InstaDownloaderDB")

# ===============================
# Force Subscribe Channel
# ===============================
auth_channel = os.getenv("AUTH_CHANNEL")
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# ===============================
# Captions
# ===============================
DEFAULT_CAPTION = os.getenv("DEFAULT_CAPTION", "Downloaded via Insta Downloader Bot 🤖")
