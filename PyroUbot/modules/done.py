import asyncio
import datetime

from PyroUbot import *

__MODULE__ = "ᴅᴏɴᴇ"
__HELP__ = """
**Bantuan Untuk Done**

**Perintah:**
- **{0}done [name item],[harga] [pembayaran]**
  
**Penjelasan:**
- Gunakan perintah **{0}done [name item],[harga] [pembayaran]** untuk mengonfirmasi pembayaran. Ini berguna untuk mencatat transaksi yang telah selesai dan memastikan bahwa semua detail pembayaran tercatat dengan benar.
"""


@PY.UBOT("done")
async def done_command(client, message):
    izzy_ganteng = await message.reply("Sedang diproses...")
    await asyncio.sleep(5)
    try:
        args = message.text.split(" ", 1)
        if len(args) < 2 or "," not in args[1]:
            await message.reply_text("**ℹ️ Penggunaan**\n.done Name Item, Price, Payment")
            return

        parts = args[1].split(",", 2)

        if len(parts) < 2:
            await message.reply_text("**ℹ️ Penggunaan**\n.done Name Item, Price, Payment")
            return

        name_item = parts[0].strip()
        price = parts[1].strip()
        payment = parts[2].strip() if len(parts) > 2 else "Lainnya"
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = (
    "「 𝗧𝗥𝗔𝗡𝗦𝗔𝗞𝗦𝗜 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 」\n"
    f"📦 **Barang**: {name_item}\n"
    f"💸 **Nominal**: {price}\n"
    f"🕰️ **Waktu**: {time}\n"
    f"💳 **Payment**: {payment}\n"
    "\n"
    "✅ Terimakasih telah order"
)
        await izzy_ganteng.edit(response)

    except Exception as e:
        await izzy_ganteng.edit(f"❌ Terjadi kesalahan.")
