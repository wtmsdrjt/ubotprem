from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ʙʟᴀᴄᴋʙᴏx"
__HELP__ = """
**Bantuan Untuk Blackbox**

**Perintah:**
- **{0}blackbox**
    - Dapat membantu Anda dengan berbagai konsep pemrograman.

**Penjelasan:**
- Gunakan perintah **{0}blackbox** untuk meminta bantuan mengenai berbagai topik dan konsep dalam pemrograman.
"""


@PY.UBOT("blackbox")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>Mohon gunakan format yang benar!\nContoh : .blackbox hai"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>proccesing....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/blackbox-chat?text={a}&apikey=Boyy')

            try:
                if "message" in response.json():
                    x = response.json()["message"]                  
                    await prs.edit(
                      f"{x}"
                    )
                else:
                    await message.reply_text("No results key found in the response.")
            except KeyError:
                await message.reply_text("❌ Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
