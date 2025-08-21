import os
from dotenv import load_dotenv

# Load from config.env
load_dotenv("config.env")

# Telegram Bot Settings
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
OWNER_ID = int(os.getenv("OWNER_ID"))

# Channels
INSTA_CHANNEL = int(os.getenv("INSTA_CHANNEL"))      # For storing Instagram media
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))          # For errors, status updates

# Database
MONGO_DB_URI = os.getenv("MONGO_DB_URI")             # MongoDB connection string
DB_NAME = os.getenv("DB_NAME", "InstaDownloaderDB")  # Default DB name

# Captions
DEFAULT_CAPTION = os.getenv("DEFAULT_CAPTION", "Downloaded via Insta Downloader Bot 🤖")
