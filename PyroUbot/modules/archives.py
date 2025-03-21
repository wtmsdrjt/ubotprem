from PyroUbot.core.helpers.tools import get_data_id
from PyroUbot import *
__MODULE__ = "ᴀʀᴄʜɪᴠᴇ"
__HELP__ = """
**Bantuan Untuk Archive**

**Perintah:**
- **{0}arch**
    - Mengarchive group chat pribadi maupun channel.

- **{0}unarch**
    - Mengunarchive group chat pribadi maupun channel.

**Penjelasan:**
- Gunakan perintah **{0}arch** untuk mengarsipkan group chat atau channel yang tidak aktif, sehingga tidak muncul di daftar utama. 
- Gunakan perintah **{0}unarch** untuk mengembalikan group chat atau channel yang telah diarsipkan ke daftar utama Anda.
"""
@PY.UBOT("arch")
@PY.TOP_CMD
async def archive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) <2:
        return await message.reply(f"{ggl}Mohon gunakan arch all, users, group.")
    anjai = await message.reply(f"{prs}Sedang diproses...")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.archive_chats(anu)
    
    await anjai.edit(f"✅ {brhsl}Berhasil mengarchivekan semua {anjir}.")

@PY.UBOT("unarch")
@PY.TOP_CMD
async def unarchive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) <2:
        return await message.reply(f"{ggl}Mojon gunakan arch all, users, group.")
    anjai = await message.reply(f"{prs}Sedang diproses...")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.unarchive_chats(anu)
    await anjai.edit(f"✅ {brhsl}Berhasil mengunarchivekan semua {anjir}.")
