import os
import shutil
import instaloader
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from info import INSTA_CHANNEL as DUMP_CHANNEL
from instaloader import Post

"""@Client.on_message(filters.regex(r"https://www\.instagram\.com/") & filters.private)
async def download_instagram_content(client, message: Message):
    if message.text.startswith("/"):
        return

    try:
        url = message.text.strip()
        if not ("/reel/" in url or "/p/" in url):
            return await message.reply("**Sᴇɴᴅ A Rᴇᴇʟ Oʀ Pᴏsᴛ Lɪɴᴋ Oɴʟʏ !!! 😅**")

        processing = await message.reply("**Pʀᴏᴄᴇssɪɴɢ...👨‍💻**")
        loader = instaloader.Instaloader()
        download_dir = "downloads"
        os.makedirs(download_dir, exist_ok=True)

        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=download_dir)

        media_files = os.listdir(download_dir)
        total_photos, total_videos = 0, 0

        for file in media_files:
            path = os.path.join(download_dir, file)
            if file.endswith('.mp4'):
                await client.send_video(
                    DUMP_CHANNEL,
                    path,
                    caption=f"**Dᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ {message.from_user.mention}\n\n[Sᴏᴜʀᴄᴇ]({url})**",
                )
                await message.reply_video(path, caption="**Tʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ !!! 😍**")
                total_videos += 1
            elif file.endswith(('.jpg', '.png')):
                await client.send_photo(
                    DUMP_CHANNEL,
                    path,
                    caption=f"**Dᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ {message.from_user.mention}\n\n[Link]({url})**"
                )
                await message.reply_photo(path)
                total_photos += 1
            os.remove(path)

        shutil.rmtree(download_dir)
        await processing.delete()

        if total_photos:
            await message.reply(f"**Dᴏᴡɴʟᴏᴀᴅᴇᴅ {total_photos} Pʜᴏᴛᴏ's**")
        elif total_videos:
            await message.reply(f"**Dᴏᴡɴʟᴏᴀᴅᴇᴅ {total_videos} Vɪᴅᴇᴏ's**")
        else:
            await message.reply("**Nᴏ Mᴇᴅɪᴀ Fᴏᴜɴᴅ Tᴏ Sᴇɴᴅ ... 🤷**")

    except FloodWait as e:
        await message.reply_text(f"**FloodWait: {e.value}s**")
    except InputUserDeactivated:
        print(f"User {message.chat.id} deactivated.")
    except UserIsBlocked:
        print(f"User {message.chat.id} blocked the bot.")
    except PeerIdInvalid:
        print(f"Cannot reach {message.chat.id}.")
    except Exception as e:
        print(e)
        await message.reply_text(f"**Eʀʀᴏʀ:** `{e}`")
"""


@Client.on_message(filters.regex(r"https://www\.instagram\.com/") & filters.private)
async def download_instagram_content(client, message: Message):
    if message.text.startswith("/"):
        return

    try:
        url = message.text.strip()
        if not ("/reel/" in url or "/p/" in url):
            return await message.reply("**Sᴇɴᴅ A Rᴇᴇʟ Oʀ Pᴏsᴛ Lɪɴᴋ Oɴʟʏ !!! 😅**")

        processing = await message.reply("**Pʀᴏᴄᴇssɪɴɢ...👨‍💻**")
        loader = instaloader.Instaloader()
        download_dir = "downloads"
        os.makedirs(download_dir, exist_ok=True)

        # Extract the shortcode and download the post
        shortcode = url.split("/")[-2]
        post = Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=download_dir)

        media_files = os.listdir(download_dir)
        total_videos = 0

        for file in media_files:
            path = os.path.join(download_dir, file)
            if file.endswith('.mp4'):
                # Extract the original caption as the file name (you can clean up the caption if needed)
                #original_file_name = post.caption if post.caption else file
                #original_file_name = original_file_name.strip()  # Clean any extra spaces
                first_line = post.caption.strip().split('\n')[0] if post.caption else os.path.splitext(file)[0]

                # Prepare the caption for the message
                caption = (
                       f"**{first_line}**\n\n"
                       f"**Dᴇᴠᴇʟᴏᴘᴇʀ 👨‍💻 : [Vɪᴊᴀʏ](https://t.me/MS_Pikachu_Bot)**\n\n"
                       f"**Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🎬 : [Jᴏɪɴ Nᴏᴡ](https://t.me/MSDxBotz)**\n\n"
                       f"**Dᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ {message.from_user.mention}**\n\n"
                       f"**Sʜᴏᴡ Sᴏᴍᴇ Rᴇᴀᴄᴛɪᴏɴ !!! 😍**\n\n"
                      )

                # Send the video or image to the dump channel
                if file.endswith('.mp4'):
                    await client.send_video(DUMP_CHANNEL, path, caption=caption)

                await message.reply_video(path, caption="**Tʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ !!! 😍**") if file.endswith('.mp4') else await message.reply_photo(path, caption="**Thanks for using me ❤️**")
                total_videos += 1

            # Clean up the downloaded file
            os.remove(path)

        # Remove the downloaded directory
        shutil.rmtree(download_dir)
        await processing.delete()

        if total_videos:
            await message.reply(f"**Dᴏᴡɴʟᴏᴀᴅᴇᴅ {total_videos} Vɪᴅᴇᴏ's**")
        else:
            await message.reply("**Nᴏ Mᴇᴅɪᴀ Fᴏᴜɴᴅ Tᴏ Sᴇɴᴅ**")

    except FloodWait as e:
        await message.reply_text(f"**FloodWait: {e.value}s**")
    except InputUserDeactivated:
        print(f"User {message.chat.id} deactivated.")
    except UserIsBlocked:
        print(f"User {message.chat.id} blocked the bot.")
    except PeerIdInvalid:
        print(f"Cannot reach {message.chat.id}.")
    except Exception as e:
        print(e)
        await message.reply_text(f"**Eʀʀᴏʀ:** `{e}`")
