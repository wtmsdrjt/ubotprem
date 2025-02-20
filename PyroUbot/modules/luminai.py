import random
import requests
from PyroUbot import *

__MODULE__ = "luminai"
__HELP__ = """
**Bantuan Untuk LuminAI**

**Perintah:**
- **{0}lumin**
    - Dapat mengobrol dengan AI.

**Penjelasan:**
- Gunakan perintah **{0}lumin** untuk memulai percakapan dengan AI. Ini memungkinkan Anda untuk mendapatkan informasi atau bantuan dengan cara yang interaktif.
"""

@PY.UBOT("lumin")
async def _(client, message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format yang benar.\nContoh: <code>.lumin halo</code>"
            )
            return

        prs = await message.reply_text("<emoji id=5319230516929502602>🔍</emoji> Menjawab...")
        query = message.text.split(' ', 1)[1]
        response = requests.get(f'https://api.diioffc.web.id/api/ai/luminai?query={query}')

        try:
            data = response.json()

            if "result" in data and "message" in data["result"]:
                x = data["result"]["message"]
                await prs.edit(f"<blockquote>{x}</blockquote>")
            else:
                await prs.edit("❌ Respons API tidak memiliki data yang diharapkan.")
        except Exception as err:
            await prs.edit(f"⚠️ Terjadi kesalahan saat memproses respons API: {err}")

    except Exception as e:
        await message.reply_text(f"⚠️ Terjadi kesalahan: {e}")
