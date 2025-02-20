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
<b>Silakan lakukan pembayaran terlebih dahulu menggunakan QRIS di bawah ini.</b>

QRIS: ||https://telegra.ph//file/218804c0d32ec424b1c8f.jpg||

<b>Tekan tombol **Konfirmasi** untuk melanjutkan.</b>
""",
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(get.id, "❌ Proses dibatalkan secara otomatis karena tidak ada tanggapan.")
    
    if get.id in CONFIRM_PAYMENT:
        if not pesan.photo:
            CONFIRM_PAYMENT.remove(get.id)
            buttons = [[InlineKeyboardButton("✅ Konfirmasi Ulang", callback_data="confirm")]]
            return await bot.send_message(
                user_id,
                """
❌ <b>Pembayaran tidak dapat diproses!</b>

💬 Harap kirimkan tangkapan layar bukti pembayaran yang valid.

✅ Silakan lakukan konfirmasi ulang setelah mengirim bukti pembayaran.
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
            buttons = [
                [InlineKeyboardButton("📞 Hubungi Admin", url="https://t.me/iamcheating")]
            ]
            return await bot.send_message(
                user_id,
                f"""
✅ <b>Pembayaran Anda telah diterima!</b>

💬 Mohon tunggu 1-2 jam kerja untuk proses konfirmasi.
Harap bersabar dan jangan spam.
""",
                reply_markup=InlineKeyboardMarkup(buttons),
            )

@PY.CALLBACK("^(kurang|tambah)")
async def _(client, callback_query):
    BULAN = int(callback_query.data.split()[1])
    HARGA = 10
    QUERY = callback_query.data.split()[0]
    try:
        if QUERY == "kurang":
            if BULAN > 1:
                BULAN -= 1
                TOTAL_HARGA = HARGA * BULAN
        elif QUERY == "tambah":
            if BULAN < 12:
                BULAN += 1
                TOTAL_HARGA = HARGA * BULAN
        buttons = BTN.PLUS_MINUS(BULAN, callback_query.from_user.id)
        await callback_query.message.edit_text(
            MSG.TEXT_PAYMENT(HARGA, TOTAL_HARGA, BULAN),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
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
✅ <b>Pembayaran Anda telah berhasil dikonfirmasi!</b>

💬 Sekarang Anda dapat membuat Userbot.
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(query[2]))
        await set_expired_date(get_user.id, expired)
        return await callback_query.edit_message_text(
            f"""
✅ <b>{get_user.first_name} {get_user.last_name or ''} telah ditambahkan sebagai anggota premium.</b>
""",
        )
    if query[0] == "failed":
        buttons = [[InlineKeyboardButton("💳 Lakukan Pembayaran", callback_data="bayar_dulu")]]
        await bot.send_message(
            get_user.id,
            """
❌ <b>Pembayaran Anda tidak dapat dikonfirmasi.</b>

💬 Silakan lakukan pembayaran kembali dengan benar.
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        return await callback_query.edit_message_text(
            f"""
❌ <b>{get_user.first_name} {get_user.last_name or ''} gagal ditambahkan ke anggota premium.</b>
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