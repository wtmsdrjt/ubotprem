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

<b>💳 Metode Pembayaran:</b>
<b>• QRIS All Payment</b>
<b>🔖 Total Harga: Rp {total}.000</b>
<b>🗓️ Total Bulan: {bulan}</b>

<b>🛍 Klik tombol konfirmasi untuk melanjutkan!</b>
"""

    async def UBOT(count):
        return f"""
<b>ThreeBot ke </b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b>👤 Akun </b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b>🆔 User ID </b> <code>{ubot._ubot[int(count)].me.id}</code>
"""

    def POLICY():
        return """
<b>🤖 Three Userbot</b>

<b>🌟 Benefit Userbot</b>
Userbot ini dapat diatur sendiri tanpa watermark, memberikan kebebasan dalam mengatur jeda dan LPM sesuai kebutuhan. Mendukung fitur forward/non-forward serta pengiriman foto, simbol, dan emoji premium.  
Selain itu, userbot ini juga support berbagai format teks seperti **bold**, __underline__, `monospace`, ~~striket~~, ||spoiler||, [tautan](https://example.com), dan lain-lain.

<b>↪️ Kebijakan Pengembalian</b>
Setelah melakukan pembayaran, jika Anda belum memperoleh/menerima manfaat dari pembelian, Anda dapat menggunakan hak penggantian dalam waktu 2 hari setelah pembelian. Namun, jika Anda telah menggunakan/menerima salah satu manfaat dari pembelian, termasuk akses ke fitur pembuatan userbot, maka Anda tidak lagi berhak atas pengembalian dana.

<b>🆘 Dukungan</b>
Untuk mendapatkan dukungan, Anda dapat:
❍ Mengikuti prosedur pembelian dibot ini
❍ Resiko userbot bisa <a href=https://t.me/rawatnokos/63>Baca Disini</a> 
❍ Beli Userbot = <b>SETUJU DAN PAHAM RESIKO</b>

👉🏻 Tekan tombol <b>Lanjutkan</b> untuk menyatakan bahwa Anda telah
membaca dan menerima ketentuan ini dan melanjutkan
pembelian. Jika tidak, tekan tombol <b>Kembali.</b>
"""
