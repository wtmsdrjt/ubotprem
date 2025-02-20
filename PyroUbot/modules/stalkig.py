import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ꜱᴛᴀʟᴋɪɢ"
__HELP__ = """
**Bantuan Untuk Stalk IG**

**Perintah:**
- **{0}stalkig**  
  **Penjelasan:** Untuk stalking Instagram menggunakan username.
"""

@PY.UBOT("stalkig")
async def stalkig(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Sedang diproses...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Contoh : .stalkig cigsafterlose_")
    
    username = message.command[1]
    chat_id = message.chat.id
    url = f"https://api.betabotz.eu.org/api/stalk/ig?username={username}&apikey=Btz-bxwol"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            username = hasil['username']
            fullName = hasil['fullName']
            followers = hasil['followers']
            following = hasil['following']
            postsCount = hasil['postsCount']
            photoUrl = hasil['photoUrl']
            bio = hasil['bio']
            caption = f"""
⭐ Username: <code>{username}</code>  
⭐ Full Name: <code>{fullName}</code>  
⭐ Followers: <code>{followers}</code>  
⭐ Following: <code>{following}</code>  
⭐ Posts: <code>{postsCount}</code>  
⭐ Bio: <code>{bio}</code>  
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
