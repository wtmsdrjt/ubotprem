from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<b>⚠️ Pemberitahuan</b>
<b>Akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>ID:</b> <code>{X.me.id}</code>
<b>Masa Aktif Telah Habis</b>
"""

    def START(message):
        return f"""
<b>👋🏻 Halo <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!</b>

<b>🤖 @{bot.me.username} adalah bot yang dapat membantu Anda membuat userbot dengan mudah.</b>

🚀 Bot ini dikembangkan oleh <a href=tg://openmessage?user_id={OWNER_ID}>@iamcheating</a>. Jika Anda mengalami kesalahan atau masalah, silakan hubungi pemilik bot tersebut.

<a href=https://t.me/UserbotStore/5>📋 Daftar Harga Userbot</a>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<b>💬 Silakan melakukan pembayaran terlebih dahulu</b>

<b>🎟️ Harga Perbulan: {harga}.000</b>

<b>💳 Metode Pembayaran</b>
QRIS [ <a href=https://t.me/UserbotStore/5>Tap Disini</a> ]

<b>🔖 Total Harga: Rp {total}.000</b>
<b>🗓️ Total Bulan: {bulan}</b>

<b>🛍 Klik tombol **Konfirmasi** untuk melanjutkan.</b>
"""

    async def UBOT(count):
        return f"""
<b>ThreeBot ke </b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b>👤 Akun </b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b>🆔 User ID </b> <code>{ubot._ubot[int(count)].me.id}</code>
"""

    def POLICY():
        return f"""
<b>🤖 Three Userbot</b>

<b>🌟 Keunggulan</b>  
Tanpa watermark, bebas atur jeda & LPM, support forward/non-forward, serta berbagai format teks (**bold**, `monospace`, ~~striket~~, dll.).  

<b>↪️ Kebijakan Pengembalian</b>  
Refund hanya berlaku dalam 2 hari jika belum menikmati manfaat pembelian. Jika sudah digunakan, refund tidak tersedia.  

<b>🆘 Dukungan</b>  
- Ikuti prosedur pembelian di bot.  
- Pahami risiko userbot <a href=https://t.me/rawatnokos/63>disini</a>.  
- Beli = <b>SETUJU & PAHAM RISIKO</b>.  

👉🏻 Klik <b>Lanjutkan</b> jika setuju, atau <b>Kembali</b> untuk batal.  
"""
