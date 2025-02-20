from PyroUbot import *
from pyrogram.raw.functions.contacts import GetBlocked

__MODULE__ = "ʙʟᴏᴄᴋᴇᴅ"
__HELP__ = """
**Bantuan Untuk Blocked**

**Perintah:**
- **{0}unblockall**
    - Menghapus blokir dari semua pengguna di daftar kontak.

- **{0}getblock**
    - Melihat jumlah pengguna yang diblokir di kontak Anda.

**Penjelasan:**
- Gunakan perintah **{0}unblockall** untuk menghapus blokir dari semua kontak yang terdaftar, dan **{0}getblock** untuk mengetahui berapa banyak pengguna yang telah Anda blokir. Ini akan membantu Anda mengelola daftar kontak dengan lebih baik.
"""

@PY.UBOT("unblockall")
async def _(user, message):
    sks = await EMO.BERHASIL(user)
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"{prs}Sedang melakukan unblockall...")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    for x in user_ids:
        try:
            await user.unblock_user(x)
        except:
            pass
    await _prs.edit(f"{sks}✅ Berhasil melakukan unblockall users.")

@PY.UBOT("getblock")
async def _(user, message):
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"{prs}sedang mengecek...")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    teko = len(user_ids)
    if user_ids:
        try:
            await _prs.edit(f"✅ Kamu memblockir : {teko} users.")
        except Exception as i:
            await _prs.edit(f"{i}")
    else:
        await _prs.edit(f"❌ Tidak ada yang di blokir.")
