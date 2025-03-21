from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ʙɪɴɢ ᴀɪ"
__HELP__ = """
**Bantuan Untuk Bing AI**

**Perintah:**
- **{0}bing**
    - Dapat mencari informasi terbaru dari web, membantu dengan tugas produktivitas seperti membuat daftar, mengatur jadwal, merekomendasikan wisata, buku, film, dan lain-lain.

**Penjelasan:**
- Gunakan perintah **{0}bing** untuk meminta Bing AI mencari informasi terkini, mengelola tugas harian, atau memberikan rekomendasi sesuai kebutuhan Anda.
"""


@PY.UBOT("bing")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>Mohon gunakan format yang benar!\nContoh : .bard query"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5469745532693923461>♾</emoji>Sedang diproses....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/bing-chat?text={a}&apikey=Boysz')

            try:
                if "message" in response.json():
                    x = response.json()["message"]                  
                    await prs.edit(
                      f"{x}"
                    )
                else:
                    await message.reply_text("❌ No results key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
