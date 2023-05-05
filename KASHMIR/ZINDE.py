from pyrogram import filters
from pyrogram import Client as suhaib



@suhaib.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    await message.reply_text("ASALAM ALAIKUM HABIBI")
