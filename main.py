from pyrogram import Client, filters
from pyrogram.types import Message
from keep_alive import keep_alive
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client("mohanlpk_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply("👋 Hello! mohanlpk bot is alive!")

keep_alive()  # Flask server for uptime
bot.run()
