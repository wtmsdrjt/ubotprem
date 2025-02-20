import asyncio

from pyrogram.errors import FloodWait

from PyroUbot import *

spam_taksdb = {}

kontol = False

__MODULE__ = "ꜱᴘᴀᴍ 2"
__HELP__ = """
**Bantuan Untuk Spam 2**

**Perintah:**
- **{0}sdspm** [Waktu] [Balas ke pesan]  
    **Penjelasan:** Memulai spam ke database. Gunakan perintah ini untuk mulai mengirim spam ke grup yang ditentukan dalam database dengan waktu yang ditentukan.

- **{0}stdspm**  
    **Penjelasan:** Menghentikan proses spam di database. Dengan perintah ini, Anda dapat menghentikan semua proses spam yang sedang berjalan di database.

- **{0}listspm**  
    **Penjelasan:** Melihat daftar grup di dalam database. Gunakan perintah ini untuk menampilkan semua grup yang telah terdaftar dalam database spam.

- **{0}addspm**  
    **Penjelasan:** Menambahkan grup ke dalam database spam. Dengan perintah ini, Anda dapat menambahkan grup baru untuk menerima spam.

- **{0}delspm**  
    **Penjelasan:** Menghapus grup dari database spam. Gunakan perintah ini untuk menghapus grup yang tidak lagi ingin Anda spam dari database.
"""


@PY.UBOT("sdspm")
async def _(c, m):
    global kontol

    if not m.reply_to_message:
        return await m.reply("Mohon balas pesan.")
    if len(m.command) != 2:
        return await m.reply("Mohon balas pesan dan berikan waktu delay.")
    try:
        interval = int(m.command[1])
    except ValueError:
        return await m.reply("Waktu delay harus berupa angka.")

    scheduled_message = m.reply_to_message
    chat_ids = monggo.ambil_spdb(c.me.id)
    kontol = True
    for chat_id in chat_ids:
        if not kontol:
            break
        if interval < 10:
            await m.reply(
                f"Minimal waktu delay 10 detik."
            )
        else:

            async def send_scheduled_message(chat_id):
                try:
                    while True:
                        await asyncio.sleep(interval)
                        await scheduled_message.copy(chat_id)
                except FloodWait:
                    if chat_id in spam_taksdb:
                        task = spam_taksdb[chat_id]
                        task.cancel()
                        del spam_taksdb[chat_id]

            task = asyncio.create_task(send_scheduled_message(chat_id))
            spam_taksdb[chat_id] = task
    kontol = False
    await m.reply(f"Berhasil menyimpan waktu delay.")


@PY.UBOT("stdspm")
async def _(c, m):
    global kontol
    if not kontol:
        return await m.reply_text(
            "❌ Tidak ada pengiriman spam yang sedang berlangsung."
        )
    chat_ids = monggo.ambil_spdb(c.me.id)
    for chat_id in chat_ids:
        if chat_id in spam_taksdb:
            task = spam_taksdb[chat_id]
            task.cancel()
            del spam_taksdb[chat_id]
    kontol = False
    await m.reply("Spam dihentikan.")


@PY.UBOT("listspm")
async def _(c, m):
    teks = "📋 **Daftar Database Spam**\n\n"
    user_id = c.me.id
    lists = monggo.ambil_spdb(user_id)
    if len(lists) == 0:
        await m.reply("Database kosong.")
    else:
        for count, chat_id in enumerate(lists, 1):
            teks += f"{count}. <code>{chat_id}</code>\n"
        await m.reply(teks)


@PY.UBOT("addspm|delspm")
async def _(c, m):
    user_id = c.me.id
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    mmk = await m.reply("Sedang diproses...")
    if m.command[0] == "addspm":
        monggo.tambah_spdb(user_id, chat_id)
        return await mmk.edit(
            f"{chat_id} Berhasil ditambahkan ke database."
        )
    elif m.command[0] == "delspm":
        monggo.kureng_spdb(user_id, chat_id)
        return await mmk.edit(
            f"{chat_id} Berhasil diuapus dari database."
        )
    else:
        return await mmk.edit(f"Silakan ketik <code>{m.text}.</code>")
