import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋɢʜ"
__HELP__ = """
**Bantuan Untuk Stalk GH**

**Perintah:**
- **{0}stalkgh**  
  **Penjelasan:** Untuk stalk GitHub menggunakan username.
"""

@PY.UBOT("stalkgh")
async def stalkgh(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Sedang diproses...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Contoh : .stalkgh wtmsdrjt")
    
    username = message.command[1]
    chat_id = message.chat.id
    url = f"https://api.betabotz.eu.org/api/stalk/github?username={username}&apikey=Btz-bxwol"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'result' in data and 'user' in data['result'] and len(data['result']['user']) > 0:
                result = data['result']['user']
                photoUrl = f"https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
                caption = f"""
👤 Nama: <code>{result['name']}</code>  
🔖 Username: <code>{result['username']}</code>  
👥 Followers: <code>{result['followers']}</code>  
👤 Following: <code>{result['following']}</code>  
📝 Bio: <code>{result['bio']}</code>  
🆔 ID Pengguna: <code>{result['idUser']}</code>
"""
                photo_path = wget.download(photoUrl)
                await client.send_photo(chat_id, caption=caption, photo=photo_path)
                if os.path.exists(photo_path):
                    os.remove(photo_path)
                
                await jalan.delete()
            else:
                await jalan.edit(f"{ggl} No channel data found.")
        else:
            await jalan.edit(f"{ggl} Failed to retrieve data. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")
