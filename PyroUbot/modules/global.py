import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.types import ChatPermissions
from PyroUbot import *


__MODULE__ = "ɢʟᴏʙᴀʟ"
__HELP__ = """
**Bantuan Untuk Global**

**Perintah:**
- **{0}gban**
    - Digunakan untuk banned user dari semua group chat.

- **{0}ungban**
    - Digunakan untuk unbanned user dari semua group chat.

- **{0}gmute**
    - Digunakan untuk mengemute user dari semua group chat yang Anda admin.

- **{0}ungmute**
    - Digunakan untuk mengungmute user dari semua group chat yang Anda admin.

**Penjelasan:**
- Dengan perintah **{0}gban**, Anda dapat melarang user tertentu untuk berpartisipasi di semua group chat.
- Perintah **{0}ungban** memungkinkan Anda untuk mengembalikan akses user yang sebelumnya dibanned.
- Gunakan **{0}gmute** untuk membisukan user di semua group chat yang Anda kelola.
- Untuk mengembalikan suara user yang dibisukan, gunakan perintah **{0}ungmute**.
"""

      

@PY.UBOT("gban")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    _msg = f"{prs} Sedang diproses..."

    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(f"{ggl} User tidak ditemukan.")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = """
🌍 Tindakan Global: {}

✅ Berhasil: {} chat  
❌ Gagal: {} chat  

👤 Pengguna: <a href='tg://user?id={}'>{} {}</a>
"""
    global_id = await get_data_id(client, "global")
    for dialog in global_id:
        if user.id == OWNER_ID:
            return await Tm.edit(f"{ggl} Tidak bisa membanned developer.")
        try:
            await client.ban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "banned", done, failed, user.id, user.first_name, (user.last_name or "")
        )
    )
    return await Tm.delete()


@PY.UBOT("ungban")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    _msg = f"{prs} Sedang diproses...."

    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(f"{ggl} User tidak ditemukan.")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = """
🌍 Tindakan Global: {}

✅ Berhasil: {} chat  
❌ Gagal: {} chat  

👤 Pengguna: <a href='tg://user?id={}'>{} {}</a>
"""
    global_id = await get_data_id(client, "global")
    for dialog in global_id:
        try:
            await client.unban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "unbanned",
            done,
            failed,
            user.id,
            user.first_name,
            (user.last_name or ""),
        )
    )
    return await Tm.delete()

@PY.UBOT("gmute")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    _msg = f"{prs}proceꜱꜱing..."

    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(f"{ggl} User tidak ditemukan.")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = """
🌍 Tindakan Global: {}

✅ Berhasil: {} chat  
❌ Gagal: {} chat  

👤 Pengguna: <a href='tg://user?id={}'>{} {}</a>
"""
    global_id = await get_data_id(client, "group")
    for dialog in global_id:
        if user.id == OWNER_ID:
            return await Tm.edit(f"{ggl} Tidak bisa membanned developer.")
        try:
            await client.restrict_chat_member(dialog, user.id, ChatPermissions(can_send_messages=False))
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "mute", done, failed, user.id, user.first_name, (user.last_name or "")
        )
    )
    return await Tm.delete()

@PY.UBOT("ungmute")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    _msg = f"{prs}proceꜱꜱing..."
    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(f"{ggl} User tidak ditemukan.")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = """
🌍 Tindakan Global: {}

✅ Berhasil: {} chat  
❌ Gagal: {} chat  

👤 Pengguna: <a href='tg://user?id={}'>{} {}</a>
"""
    global_id = await get_data_id(client, "global")
    for dialog in global_id:
        try:
            await client.restrict_chat_member(dialog, user.id, ChatPermissions(can_send_messages=True))
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "ungmuted",
            done,
            failed,
            user.id,
            user.first_name,
            (user.last_name or ""),
        )
    )
    return await Tm.delete()
