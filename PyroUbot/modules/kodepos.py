from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴋᴏᴅᴇ ᴘᴏs"
__HELP__ = """
**Bantuan Untuk Kodepos**

**Perintah:**
- **{0}kdps**
    - Dapat membantu melihat kode pos suatu desa.

**Penjelasan:**
- Gunakan perintah **{0}kdps** untuk mengetahui kode pos dari desa yang Anda cari. Ini akan memudahkan Anda dalam menemukan informasi yang diperlukan.
"""


@PY.UBOT("kdps")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format yang benar!\nContoh : .kdps nama desa"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji> Sedang diproses...")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/kodepos?query={a}&apikey=Boyy')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"{x}"
                    )
                else:
                    await message.reply_text("No results key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
