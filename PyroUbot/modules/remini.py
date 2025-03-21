import aiohttp
import filetype
import requests
from io import BytesIO
from PyroUbot import *

__MODULE__ = "ʀᴇᴍɪɴɪ"
__HELP__ = """
**Bantuan Untuk Remini**

**Perintah:**
- **{0}remini** [reply to photo]  

**Penjelasan:** 
- Untuk menghidupkan/halsukan gambar. Gunakan perintah ini untuk meningkatkan kualitas foto yang Anda balas, sehingga gambar tersebut terlihat lebih jelas dan tajam.    
"""

async def upload_media(message):
    media = await message.reply_to_message.download()
    url = "https://catbox.moe/user/api.php"

    async with aiohttp.ClientSession() as session:
        # Cek apakah media adalah objek file atau path
        if isinstance(media, str):
            # Jika media adalah path file
            with open(media, "rb") as file:
                files = {"file": file}
                async with session.post(url, data=files) as response:
                    if response.status == 200:
                        data = await response.json()
                        link = data["fileInfo"]["url"]
                        return link
                    else:
                        return f"Error: {response.status}, {await response.text()}"
        else:
            # Jika media adalah objek file
            files = {"file": media}
            async with session.post(url, data=files) as response:
                if response.status == 200:
                    data = await response.json()
                    link = data["fileInfo"]["url"]
                    return link
                else:
                    return f"Error: {response.status}, {await response.text()}"

@PY.UBOT("remini|hd")
async def _(client, message):
    try:
        if not message.reply_to_message:
            return await message.reply("Silakan balas gambar yang ingin dihaluskan.")
        
        reply_message = message.reply_to_message
        xx = await message.reply("Sedang diproses...")
        
        foto = await upload_media(message)
        if not foto:
            await xx.edit("Mohon reply foto fotonya.")
            return
        
        api_url = f'https://api.botcahx.eu.org/api/tools/remini?url={foto}&apikey=Boyy'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as api_response:
                if api_response.status != 200:
                    await xx.edit(f"Failed to fetch image: HTTP {api_response.status}")
                    return
                
                image = await api_response.json()
                url = image.get("url")
                if url:
                    await client.send_photo(message.chat.id, url, caption='Powered by @ThreeUserbot')
                    await xx.delete()
                else:
                    await xx.edit('Image URL not found in the response.')
    
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
