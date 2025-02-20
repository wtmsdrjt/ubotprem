import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋʏᴛ"
__HELP__ = """
**Bantuan Untuk Stalk YT**

**Perintah:**
- **{0}stalkyt**  
  **Penjelasan:** Untuk stalk YouTube menggunakan username.
"""

@PY.UBOT("stalkyt")
async def stalkyt(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Sedang diproses...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Contoh : .stalkyt windahbasudara")
    
    username = message.command[1]
    chat_id = message.chat.id
    url = f"https://api.betabotz.eu.org/api/stalk/yt?username={username}&apikey=Btz-bxwol"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'result' in data and 'data' in data['result'] and len(data['result']['data']) > 0:
                first_channel = data['result']['data'][0]
                photoUrl = first_channel['avatar']
                description = first_channel.get('description', 'no desk')
                caption = f"""
📺 Nama Channel: <code>{first_channel['channelName']}</code>  
👥 Subscriber: <code>{first_channel['subscriberH']}</code>  
📝 Deskripsi: <code>{description}</code>  
🔗 URL: <code>{first_channel['url']}</code>  
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
