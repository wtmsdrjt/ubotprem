import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ɢᴇᴍᴘᴀ"
__HELP__ = """
**Bantuan Untuk Gempa**

**Perintah:**
- **{0}gempa**
    - Digunakan untuk cek info sekitar gempa dari BMKG.

**Penjelasan:**
- Gunakan perintah **{0}gempa** untuk mendapatkan informasi terkini mengenai aktivitas gempa di wilayah Anda. Ini berguna untuk mengetahui kejadian seismik yang mungkin terjadi di sekitar Anda.
"""

@PY.UBOT("gempa")
async def stalkig(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    chat_id = message.chat.id
    url = f"https://api.botcahx.eu.org/api/search/gempa?apikey=Boysz"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']['result']
            lintang = hasil['Lintang']
            bujur = hasil['Bujur']
            magnitude = hasil['Magnitudo']
            kedalaman = hasil['Kedalaman']
            potensi = hasil['Potensi']
            wilayah = hasil['Wilayah']
            tanggal = hasil['tanggal']
            jam = hasil['jam']
            photoUrl = f"https://warning.bmkg.go.id/img/logo-bmkg.png"
            caption = f"""
📊 **Info Gempa Terkini**
🌍 Magnitude: {magnitude}
🌊 Kedalaman: {kedalaman}
📍 Koordinat: {bujur}, {lintang}
🕒 Waktu: {tanggal}, {jam}
🌐 Lokasi: {wilayah}
⚠️ Potensi: {potensi}
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No result key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Gagal mendapatkan data gempa.")
    
    except Exception as e:
        await jalan.edit(f"{ggl} Terjadi kesalahan.")
