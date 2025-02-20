import aiohttp
from PyroUbot import *

__MODULE__ = "ɢᴏᴏɢʟᴇ"
__HELP__ = """
**Bantuan Untuk Google**

**Perintah:**
- **{0}google [query]**
    - Digunakan untuk melakukan pencarian di Google.

**Penjelasan:**
- Gunakan perintah **{0}google [query]** untuk mencari informasi di Google sesuai dengan kata kunci yang Anda masukkan. Ini memudahkan Anda untuk mendapatkan informasi yang Anda butuhkan dengan cepat.
"""

@PY.UBOT("gg|google|googlesearch")
async def google_search(client, message):
    webevent = await message.reply("Menelusuri google...")
    match = get_arg(message)
    if not match:
        return await webevent.edit(f"{message.text} ǫᴜᴇʀʏ")
    
    search_query = match.strip()
    api_url = f"https://api.botcahx.eu.org/api/search/google?text1={search_query}&apikey=Boysz"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                gresults = await response.json()
                msg = ""
                for result in gresults.get("result", []):
                    try:
                        title = result.get("title")
                        link = result.get("link")
                        desc = result.get("description")
                        msg += f"""
<b>- {title}</b>  
🔗 <a href="{link}">Sumber</a>  

{desc}
"""
                    except Exception as e:
                        print(f"Error processing result: {e}")
                
                return await webevent.edit(
                    "\n\n**📋 Result**\n"
                    f"{msg}",
                    disable_web_page_preview=True,
                )
            else:
                return await webevent.edit("❌ Gagal mendapatkan data.")
