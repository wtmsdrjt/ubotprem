import asyncio
import random

from gc import get_objects
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from pyrogram.errors.exceptions import FloodWait

from PyroUbot import *

__MODULE__ = "ʙʀᴏᴀᴅᴅʙ"
__HELP__ = """
**Bantuan Untuk Broaddb**

**Perintah:**
- **{0}gikesdb**
    - Mengirim pesan siaran grup atau pesan database.

- **{0}adddb**
    - Menambahkan database untuk broadcast.

- **{0}undb**
    - Menghapus database broadcast.

- **{0}listdb**
    - Melihat total database broadcast yang ada.

- **{0}ralldb**
    - Menghapus semua database broadcast.

**Penjelasan:**
Gunakan perintah-perintah di atas untuk mengelola database broadcast Anda dengan mudah. Anda dapat mengirim pesan, menambah atau menghapus database, serta melihat total database yang tersedia. Jika Anda ingin menghapus semua database, cukup gunakan perintah terakhir. Semoga ini membantu!
"""

@PY.UBOT("gikesdb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)
    _msg = f"{prs} Sedang diproses..."
    gcs = await message.reply(_msg)
    if not message.reply_to_message:
        return await gcs.edit(f"**{ggl} Mohon balas ke pesan.**")
    text = message.reply_to_message
    database = await get_list_from_vars(client.me.id, "DB_ID")
    done = 0
    failed = 0
    for chat_id in database:
        try:
            await text.copy(chat_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await text.copy(chat_id)
            done += 1
        except Exception:
            failed += 1
            pass
    if client.me.is_premium:
        await gcs.delete()
        _gcs = f"""
{brhsl} Berhasil kirim ke {done} chat database
{ggl} Gagal kirim ke {failed} chat database
"""
    else:
        await gcs.delete()
        _gcs = f"""
Gcast telah selesai.
Berhasil {done} chat database
Gagal {failed} chat database
"""
    return await message.reply(_gcs)

@PY.UBOT("adddb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BERHASIL(client)
    _msg = f"{prs} Sedang diproses..."

    msg = await message.reply(_msg)
    try:
        chat_id = message.chat.id
        database = await get_list_from_vars(client.me.id, "DB_ID")

        if chat_id in database:
            txt = f"""
{grp} Sudah ada dalam database broadcaꜱt.
"""
        else:
            await add_to_vars(client.me.id, "DB_ID", chat_id)
            txt = f"""
{grp} Berhaꜱil di tambahkan ke database broadcaꜱt.
"""

        return await msg.edit(txt)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("undb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BERHASIL(client)
    _msg = f"{prs} Sedang diproses..."

    msg = await message.reply(_msg)
    try:
        chat_id = get_arg(message) or message.chat.id
        database = await get_list_from_vars(client.me.id, "DB_ID")

        if chat_id not in database:
            response = f"""
{grp} Tidak ada di daftar database broadcaꜱt.
"""
        else:
            await remove_from_vars(client.me.id, "DB_ID", chat_id)
            response = f"""
{grp}b Berhaꜱil dihapuꜱ dalam database broadcaꜱt.
"""

        return await msg.edit(response)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("listdb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs} Sedang diproses..."
    mzg = await message.reply(_msg)

    database = await get_list_from_vars(client.me.id, "DB_ID")
    total_database = len(database)

    list = f"{brhsl} Daftar Database\n"

    for chat_id in database:
        try:
            chat = await client.get_chat(chat_id)
            list += f"{chat.title} | {chat.id}\n"
        except:
            list += f"{chat_id}\n"

    list += f"{ktrng} Total database {total_database}"
    return await mzg.edit(list)


@PY.UBOT("ralldb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    _msg = f"{prs} Sedang diproses..."

    msg = await message.reply(_msg)
    databases = await get_list_from_vars(client.me.id, "DB_ID")

    if not databases:
        return await msg.edit(f"{ggl} Database broadcaꜱt Anda koꜱong.")

    for chat_id in databases:
        await remove_from_vars(client.me.id, "DB_ID", chat_id)

    await msg.edit(f"{brhsl} Semua database broadcaꜱt berhaꜱil di hapuꜱ.")
