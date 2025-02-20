import aiohttp
from bs4 import BeautifulSoup
from PyroUbot import *

__MODULE__ = "ᴡɪᴋɪᴘᴇᴅɪᴀ"
__HELP__ = """
**Bantuan Untuk Wikipedia**

**Perintah:**
- **{0}wikipedia**  
  **Penjelasan:** Wikipedia menyediakan informasi tentang berbagai topik, mulai dari sejarah, sains, budaya, hingga teknologi.
"""

async def wikipedia(query):
    try:
        url = f"https://id.wikipedia.org/wiki/{query}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return {'status': response.status, 'Pesan': 'Tidak Ditemukan'}
                page_content = await response.text()
                soup = BeautifulSoup(page_content, 'html.parser')          
                title = soup.find(id="firstHeading").get_text().strip()    
                thumb_tag = soup.select_one('#mw-content-text .mw-parser-output > div:nth-child(1) > table img')
                thumb = "https:" + thumb_tag['src'] if thumb_tag else "https://k.top4top.io/p_2121ug8or0.png"
                
                paragraphs = soup.select('#mw-content-text .mw-parser-output > p')
                content = "\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
                
                return {
                    'status': response.status,
                    'result': {
                        'judul': title,
                        'thumb': thumb,
                        'isi': content
                    }
                }
    except Exception as e:
        return {'status': 404, 'Pesan': str(e)}


@PY.UBOT("wikipedia")
async def wiki_handler(client, message):
    text = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else None
    if not text:
        await message.reply_text('Contoh : .wikipedia apa itu presiden')
        return
            
    res = await wikipedia(text)    
    if res['status'] == 200:
        result = res['result']
        caption = f"""
<emoji id=5231200819986047254>📌</emoji> <b>Judul:</b> {result['judul']}

<emoji id=5282843764451195532>📝</emoji> <b>Penjelasan:</b>
{result['isi']}
"""

        if len(caption) > 1024:
            caption = caption[:1000] + '...'

        await client.send_photo(
            message.chat.id,
            photo= f"https://itzpire.com/file/540429176594.jpg",
            caption=caption
        )
    else:
        await message.reply_text('Hasil tidak ditemukan.')
