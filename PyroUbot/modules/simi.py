from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "sɪᴍɪ ᴀɪ"
__HELP__ = """
**Bantuan Untuk Simi AI**

**Perintah:**
- **{0}simi**  
  **Penjelasan:** Dapat mengobrol, tapi agak toxic. Gunakan perintah ini untuk berinteraksi dengan Simi AI, yang dapat memberikan tanggapan dalam bentuk percakapan, meskipun terkadang bisa bersifat sarkastik atau tidak sopan.
"""


@PY.UBOT("simi")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>Mohon gunakan format yang benar!\nContoh : .simi query"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji>Menjawab....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/simsimi?query={a}&apikey=Boyy')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"{x}"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
