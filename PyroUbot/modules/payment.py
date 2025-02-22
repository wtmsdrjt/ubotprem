import asyncio
from datetime import datetime

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import *

CONFIRM_PAYMENT = []

@PY.CALLBACK("^confirm")
async def _(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await bot.get_users(user_id)
    CONFIRM_PAYMENT.append(get.id)
    try:
        await callback_query.message.delete()
        pesan = await bot.ask(
            user_id,
            f"""
Silakan kirimkan bukti pembayaran Anda dalam bentuk tangkapan layar, {full_name}.
Jika pembayaran belum dikonfirmasi, silakan hubungi @rixzbotz.
            """,
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(get.id, "Permintaan konfirmasi otomatis dibatalkan karena waktu habis.")
    
    if get.id in CONFIRM_PAYMENT:
        if not pesan.photo:
            CONFIRM_PAYMENT.remove(get.id)
            buttons = [[InlineKeyboardButton("✅ Konfirmasi", callback_data="confirm")]]
            return await bot.send_message(
                user_id,
                """
Tidak dapat diproses. Harap kirimkan tangkapan layar bukti pembayaran yang valid.
Silakan lakukan konfirmasi ulang pembayaran Anda.
                """,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        elif pesan.photo:
            buttons = BTN.ADD_EXP(get.id)
            await pesan.copy(
                OWNER_ID,
                reply_markup=buttons,
            )
            CONFIRM_PAYMENT.remove(get.id)
            buttons = [[InlineKeyboardButton("📞 Hubungi Pemilik", url=f"tg://openmessage?user_id={OWNER_ID}")]]
            return await bot.send_message(
                user_id,
                f"""
Terima kasih, {full_name}. Silakan tunggu, pembayaran Anda akan dikonfirmasi dalam waktu 1 hingga 12 jam kerja.
                """,
                reply_markup=InlineKeyboardMarkup(buttons),
            )

@PY.CALLBACK("^(kurang|tambah)")
async def _(client, callback_query):
    BULAN = int(callback_query.data.split()[1])
    HARGA = 10
    QUERY = callback_query.data.split()[0]
    try:
        if QUERY == "kurang" and BULAN > 1:
            BULAN -= 1
        elif QUERY == "tambah" and BULAN < 12:
            BULAN += 1
        TOTAL_HARGA = HARGA * BULAN
        buttons = Button.plus_minus(BULAN, callback_query.from_user.id)
        await callback_query.message.reply_text(
            MSG.TEXT_PAYMENT(HARGA, TOTAL_HARGA, BULAN),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        await callback_query.message.delete()
    except:
        pass

@PY.CALLBACK("^(success|failed|home)")
async def _(client, callback_query):
    query = callback_query.data.split()
    get_user = await bot.get_users(query[1])
    
    if query[0] == "success":
        buttons = [[InlineKeyboardButton("🔥 Buat Userbot 🔥", callback_data="buat_ubot")]]
        await bot.send_message(
            get_user.id,
            """
Pembayaran Anda telah berhasil dikonfirmasi. Sekarang Anda dapat membuat userbot.
            """,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        await add_to_vars(client.me.id, "PREM_USERS", get_user.id)
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(query[2]))
        await set_expired_date(get_user.id, expired)
        return await callback_query.edit_message_text(
            f"""
{get_user.first_name} {get_user.last_name or ''} telah ditambahkan sebagai anggota premium.
            """,
        )
    
    if query[0] == "failed":
        buttons = [[InlineKeyboardButton("💳 Lakukan Pembayaran", callback_data="bayar_dulu")]]
        await bot.send_message(
            get_user.id,
            """
Pembayaran Anda tidak dapat dikonfirmasi. Silakan lakukan pembayaran dengan benar.
            """,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        return await callback_query.edit_message_text(
            f"""
{get_user.first_name} {get_user.last_name or ''} tidak ditambahkan sebagai anggota premium.
            """,
        )
    
    if query[0] == "home":
        if get_user.id in CONFIRM_PAYMENT:
            CONFIRM_PAYMENT.remove(get_user.id)
        buttons_home = BTN.START(callback_query)
        return await callback_query.edit_message_text(
            MSG.START(callback_query),
            reply_markup=InlineKeyboardMarkup(buttons_home),
        )
