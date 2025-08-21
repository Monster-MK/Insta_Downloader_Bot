import os
from dotenv import load_dotenv

# Load from config.env
load_dotenv("config.env")

# Telegram Bot Settings
BOT_TOKEN = os.getenv("8369660708:AAHeMEjpIj8r9J9EXp4n4E5z0FQIwdtW-zs")
API_ID = int(os.getenv("20517170"))
API_HASH = os.getenv("f09e5c91dd864f01063ff63827832137")
OWNER_ID = int(os.getenv("8060684565"))

PICS = (environ.get('PICS', 'https://files.catbox.moe/7ugjlq.jpg')).split()  # Sample pic

# Channels
INSTA_CHANNEL = int(os.getenv("-1002527891441"))      # For storing Instagram media
LOG_CHANNEL = int(os.getenv("-1002845044839"))          # For errors, status updates

# Database
MONGO_DB_URI = os.getenv("mongodb+srv://mdhanush8377:9cQl4L7iYAcXxggI@cluster0.wvfwtg9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")             # MongoDB connection string
DB_NAME = os.getenv("DB_NAME", "InstaDownloaderDB")  # Default DB name

# Captions
DEFAULT_CAPTION = os.getenv("DEFAULT_CAPTION", "Downloaded via Insta Downloader Bot 🤖")
