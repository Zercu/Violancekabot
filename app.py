from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls, idle
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import AudioPiped
import os
import yt_dlp

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Get API credentials from environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME")

# Admin user IDs
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split()))

# Support group and donation link
SUPPORT_GROUP_LINK = os.getenv("SUPPORT_GROUP_LINK")
DONATION_LINK = os.getenv("DONATION_LINK")

# Initialize the Pyrogram client
app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Initialize the PyTgCalls client
pytgcalls = PyTgCalls(app)

# Check if a user is an admin
def is_admin(user_id):
    return user_id in ADMIN_IDS

# Command to start the bot
@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text("🎵 Welcome to the Telegram VC Music Bot! Use /play <song name> to play music.")

# Function to search and download a song from YouTube
def download_youtube_audio(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(f"ytsearch:{query}", download=True)
        video_title = info_dict['entries'][0]['title']
        file_path = ydl.prepare_filename(info_dict['entries'][0]).replace('.webm', '.mp3')
        
    return video_title, file_path

# Command to play music in VC
@app.on_message(filters.command("play") & filters.user(ADMIN_IDS))
async def play(client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a song name or URL.")
        return

    query = message.text.split(None, 1)[1]
    
    await message.reply_text(f"🔍 Searching for {query} on YouTube...")
    
    try:
        song_title, file_path = download_youtube_audio(query)
        await message.reply_text(f"🎶 Now playing: {song_title}")

        await pytgcalls.join_group_call(
            message.chat.id,
            InputStream(
                AudioPiped(file_path)
            )
        )
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

# Command to stop the music
@app.on_message(filters.command("stop") & filters.user(ADMIN_IDS))
async def stop(client, message: Message):
    await pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("Music stopped.")

# Command for admins to make an announcement
@app.on_message(filters.command("announce") & filters.user(ADMIN_IDS))
async def announce(client, message: Message):
    announcement_text = message.text.split(None, 1)[1] if len(message.command) > 1 else None

    if announcement_text:
        await client.send_message(message.chat.id, f"📢 Announcement: {announcement_text}")
    else:
        await message.reply_text("Please provide a message to announce.")

# Command to provide the support group link
@app.on_message(filters.command("support"))
async def support(client, message: Message):
    await message.reply_text(f"🆘 Need help? Join our support group here: {SUPPORT_GROUP_LINK}")

# Command to provide the donation link
@app.on_message(filters.command("donate"))
async def donate(client, message: Message):
    await message.reply_text(f"💸 Support the bot! Donate here: {DONATION_LINK}")

# Start the bot
if __name__ == "__main__":
    pytgcalls.start()
    idle()
    app.run()
