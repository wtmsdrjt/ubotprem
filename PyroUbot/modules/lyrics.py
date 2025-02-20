import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ʟʏʀɪᴄꜱ"
__HELP__ = """
**Bantuan Untuk Lyrics**

**Perintah:**
- **{0}lyrics**
    - Mencari lirik lagu.

**Penjelasan:**
- Gunakan perintah **{0}lyrics** untuk mencari lirik dari lagu yang Anda inginkan. Ini memudahkan Anda untuk menemukan lirik lagu dengan cepat.
"""

@PY.UBOT("lyrics")
async def lyrics(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Sedang diproses...")
    
    if len(message.command) < 2:
        return await jalan.edit("Contoh: .lyrics judul_lagu")
    
    query = ' '.join(message.command[1:])
    chat_id = message.chat.id
    url = f"https://api.betabotz.eu.org/api/search/lirik?lirik={query}&apikey=Btz-bxwol"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and data.get('status') and 'result' in data:
            hasil = data['result']
            lyrics_text = hasil.get('lyrics', 'Lirik tidak ditemukan.')
            photo_url = "https://cdn.vectorstock.com/i/1000v/71/92/music-lyrics-logo-mark-for-concert-vector-35117192.jpg"
            
            # Download gambar sementara
            photo_path = wget.download(photo_url)
            
            caption = f"""
🎵 **Lirik Lagu:** {query}

{lyrics_text}
"""
            
            await client.send_photo(chat_id, photo=photo_path, caption=caption)
            
            # Hapus file gambar setelah dikirim
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} Lirik tidak ditemukan atau respons tidak valid.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request gagal: {e}")
    except Exception as e:
        await jalan.edit(f"{ggl} Terjadi kesalahan: {e}")
