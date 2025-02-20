import os
import asyncio
import random

from os import remove
from asyncio import sleep, gather

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.enums import ChatType

from PyroUbot import *


__MODULE__ = "ᴘʀᴏꜰɪʟᴇꜱ"
__HELP__ = """
**Bantuan Untuk Profiles**

**Perintah:**
- **{0}setbio**  
    Mengubah bio pada akun Anda. Gunakan perintah ini untuk memperbarui informasi singkat tentang diri Anda, yang akan terlihat oleh orang lain di profil Anda.

- **{0}setname**  
    Mengubah nama pada akun Anda. Dengan perintah ini, Anda dapat mengganti nama tampilan di akun Telegram Anda, sehingga orang lain dapat mengenali Anda dengan lebih mudah.

- **{0}block**  
    Memblokir pengguna. Gunakan perintah ini untuk menghentikan seseorang agar tidak dapat menghubungi Anda, baik melalui pesan langsung maupun interaksi lainnya.

- **{0}unblock**  
    Membuka pemblokiran pada pengguna. Dengan perintah ini, Anda dapat mengizinkan kembali pengguna yang sebelumnya diblokir untuk menghubungi Anda.

- **{0}sg**  
    Memeriksa histori nama pengguna Telegram. Perintah ini memungkinkan Anda untuk melihat riwayat nama yang digunakan oleh pengguna tertentu, yang bisa berguna untuk mengetahui perubahan identitas mereka.

- **{0}info**  
    Melihat informasi data akun Telegram. Gunakan perintah ini untuk mendapatkan detail tentang akun Anda, termasuk informasi yang mungkin berguna untuk pengaturan privasi.

- **{0}cinfo**  
    Melihat informasi data grup/channel Telegram. Dengan perintah ini, Anda dapat mengakses informasi tentang grup atau saluran yang Anda ikuti, termasuk deskripsi dan anggota.
"""


@PY.UBOT("sg")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    get_user = await extract_user(message)
    lol = await message.reply(f"{prs} Sedang diproses...")
    if not get_user:
        return await lol.edit(f"{ggl} User tidak ditemukan.")
    try:
        user_id = (await client.get_users(get_user)).id
    except Exception:
        try:
            user_id = int(message.command[1])
        except Exception as error:
            return await lol.edit(error)
    bot = ["@Sangmata_bot", "@SangMata_beta_bot"]
    getbot = random.choice(bot)
    await client.unblock_user(getbot)
    txt = await client.send_message(getbot, user_id)
    await asyncio.sleep(4)
    await txt.delete()
    await lol.delete()
    async for name in client.search_messages(getbot, limit=2):
        if not name.text:
            await message.reply(
                f"{ggl} {getbot} Tidak dapat merespon permintaan.", quote=True
            )
        else:
            await message.reply(name.text, quote=True)
    user_info = await client.resolve_peer(getbot)
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))


@PY.UBOT("info")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    Tm = await message.reply(f"{prs} Sedang diproses...")
    if not user_id:
        return await Tm.edit(
            f"{ggl} Berikan userid/username/reply untuk mendapatkan info pengguna tersebut."
        )
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""
<b>{brhsl} Informasi Pengguna</b>
<emoji id=6030656587830399914>🆔</emoji> ID Pengguna: {user.id}  
<emoji id=5260399854500191689>😀</emoji> Nama Depan: {first_name}  
<emoji id=5257969839313526622>📂</emoji> Nama Belakang: {last_name}  
<emoji id=5258331647358540449>✍️</emoji> Username: {username}  
<emoji id=5260268501515377807>📣</emoji> DC ID: {dc_id}  
<emoji id=5258093637450866522>🤖</emoji> Bot: {user.is_bot}  
<emoji id=5219805369806629055>⚠</emoji> Akun Scam: {user.is_scam}  
<emoji id=6003779240837780921>🚫</emoji> Dibatasi: {user.is_restricted}  
<emoji id=5260341314095947411>✔</emoji> Terverifikasi: {user.is_verified}  
<emoji id=5258185631355378853>⭐️</emoji> Pengguna Premium: {user.is_premium}  
<emoji id=5292226786229236118>🔄</emoji> Bio: {bio}  
</b></blockquote>

<blockquote><b>
<emoji id=5220070652756635426>👥</emoji> Grup yang sama ditemukan: {len(common)}  
<emoji id=5253959125838090076>🕒</emoji> Terakhir Terlihat: {status}  
<emoji id=4942990428317156193>😅</emoji> Userbot: <a href=tg://user?id={user.id}>{fullname}</a>  
"""
        
        photo_id = user.photo.big_file_id if user.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"info: {e}")


@PY.UBOT("cinfo")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    Tm = await message.reply(f"{prs} Sedang diproses...")
    try:
        if len(message.text.split()) > 1:
            chat_u = message.text.split()[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await Tm.edit(
                    f"{ggl} Gunakan perintah ini di dalam grup atau gunakan cinfo [group username atau id]"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""
**Informasi Obrolan**
🆔 ID Obrolan: {chat.id}  
👥 Judul: {chat.title}  
🔗 Username: {username}  
📩 Tipe: {type}  
🏛️ DC ID: {dc_id}  
⚠️ Scam: {chat.is_scam}  
🎭 Palsu: {chat.is_fake}  
✅ Terverifikasi: {chat.is_verified}  
🚫 Dibatasi: {chat.is_restricted}  
🔰 Konten Dilindungi: {chat.has_protected_content}  

👥 Total Anggota: {chat.members_count}  
📝 Deskripsi: {description}
"""
        
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"info: `{e}`")


@PY.UBOT("id")
@PY.TOP_CMD
async def _(client, message):
    text = f"<emoji id=6026218958900695642>💎</emoji> ID Pesan : `{message.id}`\n"

    if message.chat.type == ChatType.CHANNEL:
        text += f"<emoji id=6026056450223116307>⏺</emoji> ID Chat : `{message.sender_chat.id}`\n"
    else:
        text += f"<emoji id=6026292029179301727>👑</emoji> ID Anda: `{message.from_user.id}`\n"

        if len(message.command) > 1:
            try:
                user = await client.get_chat(message.text.split()[1])
                text += f"<emoji id=6026056450223116307>⏺</emoji> ID User: `{user.id}`\n"
            except:
                return await message.reply("<emoji id=6113891550788324241>❌</emoji>Pengguna tidak ditemukan.")

        text += f"<emoji id=6026056450223116307>⏺</emoji> ID Chat : `{message.chat.id}`\n"

    if message.reply_to_message:
        id_ = (
            message.reply_to_message.from_user.id
            if message.reply_to_message.from_user
            else message.reply_to_message.sender_chat.id
        )
        file_info = get_file_id(message.reply_to_message)
        if file_info:
            text += f"Media ID: {file_info.file_id}\n\n"
        text += (
            f"<emoji id=6026257381678124710>✅</emoji> ID Pesan yang Dibalas: `{message.reply_to_message.id}`\n"
f"<emoji id=6026257381678124710>✅</emoji> ID Pengguna yang Dibalas: `{id_}`"
        )

    return await message.reply(text, disable_web_page_preview=True)


@PY.UBOT("setbio")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    tex = await message.reply(f"{prs} Sedang diproses...")
    if len(message.command) == 1:
        return await tex.edit(f"{ggl}{message.text.split()[0]} [text]")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"{brhsl} Berhasil mengubah bio menjadi {bio}")
        except Exception as e:
            await tex.edit(f"ERROR: {e}")
    else:
        return await tex.edit(f"{ggl} Berikan tekꜱ untuk ditetapkan ꜱebagai bio.")


@PY.UBOT("setname")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    tex = await message.reply(f"{prs} Sedang diproses...")
    if len(message.command) == 1:
        return await tex.edit(f"{ggl}{message.text.split()[0]} [text]")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(
                f"{brhsl} Berhasil mengubah nama menjadi {name}"
            )
        except Exception as e:
            await tex.edit(f"ERROR: {e}")
    else:
        return await tex.edit(f"{ggl} Berikan tekꜱ untuk ditetapkan ꜱebagai nama Anda.")


@PY.UBOT("block")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    tex = await message.reply(f"{prs} Sedang diproses...")
    if not user_id:
        return await tex.edit(f"{ggl}{message.text.split()[0]} [reply to user]")
    if user_id == client.me.id:
        return await tex.edit(f"{brhsl} Oke, done.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"{brhsl} Berhasil memblokir {umention}")
  

@PY.UBOT("unblock")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    tex = await message.reply(f"{prs} Sedang diproses...")
    if not user_id:
        return await tex.edit(f"{ggl} {message.text.split()[0]} [reply to user]")
    if user_id == client.me.id:
        return await tex.edit(f"{brhsl} Oke, done.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"{brhsl} Berhasil membuka blokir {umention}")

@PY.UBOT("idm")
@PY.TOP_CMD
async def _(client, message):
    if not message.reply_to_message:
        return
    id = message.reply_to_message.entities[0].custom_emoji_id
    await message.reply(f"`{id}`")

