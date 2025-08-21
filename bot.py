from pyrogram import Client, filters
from pyrogram.types import Message
from info import BOT_TOKEN, API_ID, API_HASH
from script import Script
from commands import CommandButtons

app = Client(
    "InstaDownloaderBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_text(
        Script.START_TXT.format(message.from_user.mention),
        reply_markup=CommandButtons.START_BUTTONS
    )

@app.on_message(filters.command("help") & filters.private)
async def help_command(client, message: Message):
    await message.reply_text(
        Script.HELP_TXT,
        reply_markup=CommandButtons.HELP_BUTTONS
    )

@app.on_message(filters.command("about") & filters.private)
async def about_command(client, message: Message):
    await message.reply_text(
        Script.ABOUT_TXT,
        reply_markup=CommandButtons.ABOUT_BUTTONS
    )

@app.on_message(filters.command("status") & filters.private)
async def status_command(client, message: Message):
    await message.reply_text(
        Script.STATUS_TXT.format("0h 0m", 0, 0),
        reply_markup=CommandButtons.STATUS_BUTTONS
    )

print("Bᴏᴛ Sᴛᴀʀᴛᴇᴅ Oɴ Tᴇʟᴇɢʀᴀᴍ !!! 😎💥")
app.run()
