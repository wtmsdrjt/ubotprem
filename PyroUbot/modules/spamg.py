import asyncio

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait

from .. import *
from PyroUbot import *

__MODULE__ = "ꜱᴘᴀᴍ"
__HELP__ = """
**Bantuan Untuk Spam**

**Perintah:**
- **{0}spam**  
    **Penjelasan:** Melakukan spam pesan. Gunakan perintah ini untuk mengirimkan pesan berulang kali dalam waktu singkat.

- **{0}setdelay**  
    **Penjelasan:** Mengatur delay setiap pesan yang dikirim. Dengan perintah ini, Anda dapat menentukan jeda waktu antara setiap pesan yang dikirim saat melakukan spam.

- **{0}stopspam**  
    **Penjelasan:** Memberhentikan spam pesan yang sedang berjalan. Gunakan perintah ini untuk menghentikan proses pengiriman pesan spam yang sedang berlangsung.
"""

spam_progress = []

async def SpamMsg(client, message, send):
    delay = await get_vars(client.me.id, "SPAM") or 0
    await asyncio.sleep(int(delay))
    if message.reply_to_message:
        await send.copy(message.chat.id)
    else:
        await client.send_message(message.chat.id, send)

@PY.UBOT("spam")
@PY.TOP_CMD
async def _(client, message):
    global spam_progress
    spam_progress.append(client.me.id)
    sks = await EMO.BERHASIL(client)
    _msg = "Sedang diproses..."

    r = await message.reply(_msg)
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> [jumlah] [text/reply_msg]</b>")

    if not msg:
        return await r.edit(
            f"<b><code>{message.text.split()[0]}</code> [jumlah] [text/reply_msg]</b>"
        )
    
    for _ in range(count):
        if client.me.id not in spam_progress:
            await r.edit(f"Proses spam berhasil di batalkan.")
            return
        await SpamMsg(client, message, msg)

    spam_progress.remove(client.me.id)    
    await r.edit("Spam telah selesai.")

@PY.UBOT("setdelay")
@PY.TOP_CMD
async def _(client, message):
    _msg = "Sedang diproses..."

    r = await message.reply(_msg)
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> [count]</b>")

    if not count:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> [count]</b>")

    await set_vars(client.me.id, "SPAM", count)
    return await r.edit("Delay spam berhasil disetting.")

@PY.UBOT("stopspam")
@PY.TOP_CMD
async def _(client, message):
    global spam_progress
    if client.me.id in spam_progress:
        spam_progress.remove(client.me.id)
        await message.reply("✅ Spam telah berhenti.")
    else:
        await message.reply("❌ Tidak ada spam yang ditemukan")
