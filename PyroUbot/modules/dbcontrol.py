from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone


from PyroUbot import *

__MODULE__ = "ᴅʙ ᴄᴏɴᴛʀᴏʟ"
__HELP__ = """
**Bantuan Untuk DB Control**

**Perintah:**
- **{0}time**
    - Digunakan untuk menambah atau mengurangi masa aktif user.

- **{0}cek**
    - Digunakan untuk melihat masa aktif user.

- **{0}addadmin**
    - Digunakan untuk menambahkan admin.

- **{0}unadmin**
    - Digunakan untuk menghapus admin.

- **{0}getadmin**
    - Digunakan untuk melihat daftar admin.

- **{0}seles**
    - Digunakan untuk menandai user sebagai seleb.

- **{0}unseles**
    - Digunakan untuk menghapus tanda seleb dari user.

- **{0}getseles**
    - Digunakan untuk melihat daftar user yang ditandai sebagai seleb.

**Penjelasan:**
- Gunakan perintah **{0}time** untuk mengatur masa aktif user sesuai kebutuhan. Ini berguna untuk mengelola akses user.
- Dengan perintah **{0}cek**, Anda dapat memeriksa berapa lama masa aktif user yang terdaftar.
- Perintah **{0}addadmin**, **{0}unadmin**, dan **{0}getadmin** membantu Anda dalam mengelola admin di sistem.
- Untuk menandai user sebagai seles, gunakan **{0}seles**, dan jika Anda ingin menghapus tanda tersebut, gunakan **{0}unseles**. Perintah **{0}getseles** memungkinkan Anda untuk melihat siapa saja yang telah ditandai sebagai seles.
"""

@PY.BOT("prem")
@PY.SELLER
async def _(client, message):
    user_id, get_bulan = await extract_user_and_reason(message)
    msg = await message.reply("Sedang diproses...")
    if not user_id:
        return await msg.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʙᴜʟᴀɴ</b>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    if not get_bulan:
        get_bulan = 1

    prem_users = await get_list_from_vars(client.me.id, "PREM_USERS")

    if user.id in prem_users:
        return await msg.edit(f"""
👤 Nama: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
💎 Keterangan: Sudah Premium ✅  
⏳ Expired: {get_bulan} Bulan  
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(client.me.id, "PREM_USERS", user.id)
        await msg.edit(f"""
👤 Nama: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
⏳ Expired: {get_bulan} Bulan  

📌 Silakan buka @{client.me.username} untuk membuat Userbot.  

📖 Cara Membuat Userbot:  
🔹 Silakan /start dulu bot @{client.me.username} 
🔹 Jika sudah start, tekan tombol "Buat Userbot"  
🔹 Ikuti arahan yang diberikan oleh bot.  
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"🆔 ID Seller: {message.from_user.id}\n🆔 ID Customer: {user_id}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔱 Seller",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "Customer ⚜️", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unprem")
@PY.SELLER
async def _(client, message):
    msg = await message.reply("Sedang diproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} user_id/username</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(client.me.id, "PREM_USERS")

    if user.id not in prem_users:
        return await msg.edit(f"""
**ℹ️ Information**
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
🔴 Keterangan: Tidak dalam daftar  
 """
        )
    try:
        await remove_from_vars(client.me.id, "PREM_USERS", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
**ℹ️ Information**
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
🔓 Keterangan: Unpremium  
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.BOT("getprem")
@PY.SELLER
async def _(client, message):
    text = ""
    count = 0
    prem = await get_list_from_vars(client.me.id, "PREM_USERS")
    prem_users = []

    for user_id in prem:
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"<blockquote><b>{userlist}\n</blockquote></b>"
    if not text:
        await message.reply_text("❌ Tidak ada pengguna yang ditemukan.")
    else:
        await message.reply_text(text)


@PY.BOT("seles")
@PY.ADMIN
async def _(client, message):
    msg = await message.reply("Sedang diproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} user_id/username</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if user.id in sudo_users:
        return await msg.edit(f"""
**ℹ️ Information**
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
💼 Keterangan: Sudah Seller  
"""
        )

    try:
        await add_to_vars(client.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
**ℹ️ Information**
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
💼 Keterangan: Seller  
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unseles")
@PY.ADMIN
async def _(client, message):
    msg = await message.reply("Sedang diproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} user_id/username</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    seles_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if user.id not in seles_users:
        return await msg.edit(f"""
**ℹ️ Information**
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
🔴 Keterangan: Tidak dalam daftar  
"""
        )

    try:
        await remove_from_vars(client.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
**ℹ️ Information**
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
🚫 Keterangan: Unseller  
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getseles")
@PY.ADMIN
async def _(client, message):
    Sh = await message.reply("Sedang diproses...")
    seles_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if not seles_users:
        return await Sh.edit("❌ Daftar seller kosong.")

    seles_list = []
    for user_id in seles_users:
        try:
            user = await client.get_users(int(user_id))
            seles_list.append(
                f"<b>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code></b>"
            )
        except:
            continue

    if seles_list:
        response = (
            "**📋 Daftar Seller**\n\n"
            + "\n".join(seles_list)
            + f"\n\n• Total seller: {len(seles_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("❌ Tidak dapat mengambil daftar seller.")


@PY.BOT("time")
@PY.SELLER
async def _(client, message):
    Tm = await message.reply("Sedang diproses...")
    bajingan = message.command
    if len(bajingan) != 3:
        return await Tm.edit(f"❌ Mohon gunakan /set_time user_id hari")
    user_id = int(bajingan[1])
    get_day = int(bajingan[2])
    print(user_id , get_day)
    try:
        get_id = (await client.get_users(user_id)).id
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(f"""
**ℹ️ Information**  
👤 Name: {user.mention}  
🆔 ID: {get_id}  
⏳ Aktifkan Selama: {get_day} Hari
"""
    )


@PY.BOT("cek")
@PY.SELLER
async def _(client, message):
    Sh = await message.reply("Sedang diproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await Sh.edit("❌ Pengguna tidak temukan.")
    try:
        get_exp = await get_expired_date(user_id)
        sh = await client.get_users(user_id)
    except Exception as error:
        return await Sh.ediit(error)
    if get_exp is None:
        await Sh.edit(f"""
**ℹ️ Information**  
👤 Name: {sh.mention}  
📋 Plan: None  
🆔 ID: {user_id}  
📍 Prefix: .  
⏳ Expired: Nonaktif
""")
    else:
        SH = await ubot.get_prefix(user_id)
        exp = get_exp.strftime("%d-%m-%Y")
        if user_id in await get_list_from_vars(client.me.id, "ULTRA_PREM"):
            status = "SuperUltra"
        else:
            status = "Premium"
        await Sh.edit(f"""
**ℹ️ Information**  
👤 Name: {sh.mention}  
📋 Plan: {status}  
🆔 ID: {user_id}  
📍 Prefix: {' '.join(SH)}  
⏳ Expired: {exp}
"""
        )


@PY.BOT("addadmin")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("Sedang diproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if user.id in admin_users:
        return await msg.edit(f"""
**ℹ️ Information**  
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
✅ Keterangan: Sudah dalam daftar
"""
        )

    try:
        await add_to_vars(client.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
**ℹ️ Information**  
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
🔑 Keterangan: Admin
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unadmin")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("Sedang diproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if user.id not in admin_users:
        return await msg.edit(f"""
**ℹ️ Information**  
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
❌ Keterangan: Tidak dalam daftar
"""
        )

    try:
        await remove_from_vars(client.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
**ℹ️ Information**  
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
🚫 Keterangan: Unadmin        
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getadmin")
@PY.OWNER
async def _(client, message):
    Sh = await message.reply("Sedang diproses...")
    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if not admin_users:
        return await Sh.edit("❌ Daftar admin kosong.")

    admin_list = []
    for user_id in admin_users:
        try:
            user = await client.get_users(int(user_id))
            admin_list.append(
                f"👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | {user.id}"
            )
        except:
            continue

    if admin_list:
        response = (
            "📋 **Daftar Admin**\n\n"
            + "\n".join(admin_list)
            + f"\n\n• Total admin: {len(admin_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("❌ Tidak dapat mengambil daftar admin.")

@PY.BOT("superultra")
@PY.SELLER
async def _(client, message):
    user_id, get_bulan = await extract_user_and_reason(message)
    msg = await message.reply("Sedang diproses...")
    if not user_id:
        return await msg.edit(f"{message.text} user_id/username")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    if not get_bulan:
        get_bulan = 1

    prem_users = await get_list_from_vars(client.me.id, "ULTRA_PREM")

    if user.id in prem_users:
        return await msg.edit(f"""
**ℹ️ Information**  
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: {user.id}  
✅ Keterangan: Sudah <code>[SuperUltra]</code>  
⏳ Expired: <code>{get_bulan}</code> Bulan
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(client.me.id, "ULTRA_PREM", user.id)
        await msg.edit(f"""
**ℹ️ Information**  
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: <code>{user.id}</code>  
⏳ Expired: <code>{get_bulan}</code> Bulan  
📌 Silakan buka @{client.me.mention} untuk membuat Userbot  
🔑 Status: <code>[SuperUltra]</code>
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"🆔 ID Seller: {message.from_user.id}\n🆔 ID Customer: {user_id}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔱 Seller",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "Customer ⚜️", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)

@PY.BOT("rmultra")
@PY.SELLER
async def _(client, message):
    msg = await message.reply("Sedang diproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(client.me.id, "ULTRA_PREM")

    if user.id not in prem_users:
        return await msg.edit(f"""
**ℹ️ Information**  
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: <code>{user.id}</code>  
❌ Keterangan: Tidak dalam daftar
"""
        )
    try:
        await remove_from_vars(client.me.id, "ULTRA_PREM", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
**ℹ️ Information**  
👤 Name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})  
🆔 ID: <code>{user.id}</code>  
❌ Keterangan: None SuperUltra
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.BOT("getultra")
@PY.SELLER
async def _(client, message):
    prem = await get_list_from_vars(client.me.id, "ULTRA_PREM")
    prem_users = []

    for user_id in prem:
        try:
            user = await client.get_users(user_id)
            prem_users.append(
                f"👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | {user.id}"
            )
        except Exception as error:
            return await message.reply(str(error))

    total_prem_users = len(prem_users)
    if prem_users:
        prem_list_text = "\n".join(prem_users)
        return await message.reply(
            f"📋 **Daftar Superultra**\n\n{prem_list_text}\n\n• Total superultra: {total_prem_users}"
        )
    else:
        return await message.reply("❌ Tidak ada pengguna superultra saat ini.")
