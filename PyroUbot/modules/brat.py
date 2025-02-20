import os
from PyroUbot import *
from pyrogram.enums import MessagesFilter
from pyrogram.types import *
import requests

__MODULE__ = "ʙʀᴀᴛ"
__HELP__ = """
**Bantuan Untuk Brat**

**Perintah:**
- **{0}brat [text]**
    - Digunakan untuk membuat gambar teks seperti tren di TikTok.

**Penjelasan:**
- Gunakan perintah **{0}brat [text]** untuk membuat gambar teks yang menarik, mengikuti tren yang sedang populer di TikTok. Cukup masukkan teks yang ingin Anda gunakan, dan hasilnya akan siap untuk dibagikan!
"""

def get_brat_image(text):
    url = f"https://api.betabotz.eu.org/api/maker/brat"
    params = {
        "text": text,
        "apikey": "Btz-bxwol"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
@PY.UBOT("brat")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("Gunakan perintah /brat teks untuk membuat gambar.")
        return

    request_text = args[1]
    await message.reply_text("Sedang diproses...")

    image_content = get_brat_image(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("❌ Gagal membuat gambar. Coba lagi nanti.")
