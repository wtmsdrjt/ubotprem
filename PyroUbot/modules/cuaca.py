import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ᴄᴜᴀᴄᴀ"
__HELP__ = """
**Bantuan Untuk Cuaca**

**Perintah:**
- **{0}cuaca**
    - Digunakan untuk cek info cuaca di kota-kota besar.

**Penjelasan:**
- Gunakan perintah **{0}cuaca** untuk mendapatkan informasi cuaca terkini di berbagai kota besar. Ini sangat berguna untuk merencanakan aktivitas Anda sesuai dengan kondisi cuaca.
"""

@PY.UBOT("cuaca")
async def cuaca(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Sedang diproses...")
    a = message.text.split(' ', 1)[1]
    chat_id = message.chat.id
    url = f"https://api.betabotz.eu.org/api/tools/cuaca?query={a}&apikey=Btz-bxwol"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            location = hasil['location']
            country = hasil['country']
            weather = hasil['weather']
            currentTemp = hasil['currentTemp']
            maxTemp = hasil['maxTemp']
            minTemp = hasil['minTemp']
            humidity = hasil['humidity']
            windSpeed = hasil['windSpeed']
            photoUrl = f"https://telegra.ph//file/9354c197366cde09650fd.jpg"
            caption = f"""
🌤️ <b>Info Cuaca Terkini</b> 🌍  
📍 <b>Lokasi:</b> <code>{location}</code>  
🏳️ <b>Negara:</b> <code>{country}</code>  
🌦️ <b>Cuaca:</b> <code>{weather}</code>  
🌡️ <b>Suhu Saat Ini:</b> <code>{currentTemp}°C</code>  
📊 <b>Suhu Maks/Min:</b> <code>{maxTemp}°C / {minTemp}°C</code>  
💨 <b>Kecepatan Angin:</b> <code>{windSpeed} km/h</code>  
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No result key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Gagal mendapatkan data cuaca.")
    
    except Exception as e:
        await jalan.edit(f"{ggl} Terjadi kesalahan.")
