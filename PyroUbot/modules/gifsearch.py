import random
from PyroUbot import *
from pyrogram.types import InputMediaPhoto

__MODULE__ = "ɢɪғsᴇᴀʀᴄʜ"
__HELP__ = """
**Bantuan Untuk GifSearch**

**Perintah:**
- **{0}gif [ǫᴜᴇʀʏ]**
    - Digunakan untuk mencari gif/animasi random dari Google.

**Penjelasan:**
- Gunakan perintah **{0}gif [ǫᴜᴇʀʏ]** untuk menemukan berbagai gif atau animasi yang sesuai dengan kata kunci yang Anda masukkan. Ini adalah cara yang menyenangkan untuk menemukan gambar bergerak yang dapat Anda gunakan.
"""

@PY.UBOT("gif")
async def gif_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(f"<code>{message.text}</code> [ǫᴜᴇʀʏ]")
    TM = await message.reply("Sedang diproses...")
    try:
        x = await client.get_inline_bot_results(
            message.command[0], message.text.split(None, 1)[1]
        )
        saved = await client.send_inline_bot_result(
            client.me.id, x.query_id, x.results[random.randrange(len(x.results))].id
        )
    except:
        await message.reply("❌ Gif tidak ditemukan.")
        return await TM.delete()
    saved = await client.get_messages(client.me.id, int(saved.updates[1].message.id))
    await client.send_animation(
        message.chat.id, saved.animation.file_id, reply_to_message_id=message.id
    )
    await TM.delete()
    return await saved.delete()
