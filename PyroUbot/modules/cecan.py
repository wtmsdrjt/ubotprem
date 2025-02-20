from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴄᴇᴄᴀɴ"
__HELP__ = """
**Bantuan Untuk Cecan**

**Perintah:**
- **{0}cecan [query]**

**Query:**
- **Indonesia**
- **China**
- **Thailand**
- **Vietnam**
- **Hijaber**
- **Rose**
- **Ryujin**
- **Jiso**
- **Jeni**
- **Justinaxie**
- **Malaysia**
- **Japan**
- **Korea**

**Penjelasan:**
Gunakan perintah di atas dengan menambahkan salah satu query untuk mendapatkan informasi atau konten terkait. Anda dapat memilih dari berbagai opsi yang tersedia sesuai kebutuhan Anda.
"""

URLS = {
    "indonesia": "https://api.betabotz.eu.org/api/cecan/indonesia?apikey=Btz-bxwol",
    "china": "https://api.betabotz.eu.org/api/cecan/china?apikey=Btz-bxwol",
    "thailand": "https://api.betabotz.eu.org/api/cecan/thailand?apikey=Btz-bxwol",
    "vietnam": "https://api.betabotz.eu.org/api/cecan/vietnam?apikey=Btz-bxwol",
    "hijaber": "https://api.betabotz.eu.org/api/cecan/hijaber?apikey=Btz-bxwol",
    "rose": "https://api.betabotz.eu.org/api/cecan/rose?apikey=Btz-bxwol",
    "ryujin": "https://api.betabotz.eu.org/api/cecan/ryujin?apikey=Btz-bxwol",
    "jiso": "https://api.betabotz.eu.org/api/cecan/jiso?apikey=Btz-bxwol",
    "jeni": "https://api.betabotz.eu.org/api/cecan/jeni?apikey=Btz-bxwol",
    "justinaxie": "https://api.betabotz.eu.org/api/cecan/justinaxie?apikey=Btz-bxwol",
    "malaysia": "https://api.betabotz.eu.org/api/cecan/malaysia?apikey=Btz-bxwol",
    "japan": "https://api.betabotz.eu.org/api/cecan/japan?apikey=Btz-bxwol",
    "korea": "https://api.betabotz.eu.org/api/cecan/korea?apikey=Btz-bxwol"
}

@PY.UBOT("cecan")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"❌ Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("Sedang diproses...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"❌ Gagal mengambil gambar cecan.")
