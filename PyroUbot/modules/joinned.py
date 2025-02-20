from pyrogram import *
from pyrogram import errors
from pyrogram import enums
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from PyroUbot import *

__MODULE__ = "ᴊᴏɪɴʟᴇᴀᴠᴇ"
__HELP__ = """
**Bantuan Untuk Joinleave**

**Perintah:**
- **{0}kickme**
    - Keluar dari grup Telegram.

- **{0}join**
    - Bergabung ke grup melalui tautan atau username grup.

- **{0}leaveallgc**
    - Keluar dari semua grup Telegram, kecuali untuk admin/owner.

- **{0}leaveallmute**
    - Keluar dari grup yang membatasi Anda.

- **{0}leaveallch**
    - Keluar dari semua channel, kecuali untuk admin/owner.

**Penjelasan:**
- Gunakan perintah-perintah di atas untuk mengelola keanggotaan Anda di grup dan channel Telegram dengan lebih mudah. Jika Anda ingin keluar dari grup atau bergabung dengan grup baru, cukup gunakan perintah yang sesuai.
"""


@PY.UBOT("kickme")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(f"{prs} Sedang diproses...")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit(f"{ggl} Perintah ini dilarang digunakan di grup ini.")
    try:
        await xxnx.edit_text(f"{client.me.first_name} Sayonara!")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"{ggl}Error: \n\n{str(ex)}")



@PY.UBOT("join")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(f"{prs} Sedang diproses...")
    try:
        await xxnx.edit(f"{sks} Berhaꜱil bergabung ke chat ID {Man}")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"{ggl}Error: \n\n{str(ex)}")


@PY.UBOT("leaveallgc")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = await message.reply(f"{prs} Sedang keluar dari semua grup....")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    done += 1
                    await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"{sks} Berhaꜱil keluar dari {done} grup\n{ggl} Gagal keluar dari {er} grup"
    )


@PY.UBOT("leaveallch")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = await message.reply(f"{prs} Sedang keluar dari semua channel...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.CHANNEL:
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    done += 1
                    await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"{sks} Berhaꜱil keluar dari {done} channel\n{ggl} Gagal keluar dari {er} channel"
    )

@PY.UBOT("leaveallmute")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    done = 0
    Haku = await message.reply_text(f"{prs} Sedang diproses...")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            chat_id = dialog.chat.id
            try:
                member = await client.get_chat_member(chat_id, "me")
                if member.status == ChatMemberStatus.RESTRICTED:
                    await client.leave_chat(chat_id)
                    done += 1
            except Exception:
                pass
    await Haku.edit(f"""
{sks} Berhasil keluar dari **{done}** grup yang telah membatasi Anda.
""")
