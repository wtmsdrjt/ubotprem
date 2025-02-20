import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ꜱᴛᴀʟᴋᴛᴛ"
__HELP__ = """
**Bantuan Untuk Stalk TT**

**Perintah:**
- **{0}stalktt**  
  **Penjelasan:** Untuk stalk TikTok menggunakan username.
"""

@PY.UBOT("stalktt")
async def stalktt(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Sedang diproses...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Contoh : .stalktt playboicarti")
    
    username = message.command[1]
    chat_id = message.chat.id
    url = f"https://api.betabotz.eu.org/api/stalk/tt?username={username}&apikey=Btz-bxwol"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            username = hasil['username']
            description = hasil['description']
            likes = hasil['likes']
            followers = hasil['followers']
            following = hasil['following']
            totalPosts = hasil['totalPosts']
            photoUrl = hasil['profile']
            caption = f"""
<emoji id=5841235769728962577>⭐</emoji> Username: <code>{username}</code>  
<emoji id=5843952899184398024>⭐</emoji> Deskripsi: <code>{description}</code>  
<emoji id=5841243255856960314>⭐</emoji> Jumlah Like: <code>{likes}</code>  
<emoji id=5352566966454330504>⭐</emoji> Pengikut: <code>{followers}</code>  
<emoji id=5353036831581544549>⭐</emoji> Mengikuti: <code>{following}</code>  
<emoji id=5841243255856960314>⭐</emoji> Total Postingan: <code>{totalPosts}</code>  
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No result key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")
