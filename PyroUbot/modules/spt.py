from PyroUbot import *
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

SUPPORT = []

@PY.CALLBACK("^support")
async def support_callback(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await client.get_users(user_id)
    await callback_query.message.delete()
    SUPPORT.append(get.id)
    try:
        button = [
            [InlineKeyboardButton("Batalkan", callback_data=f"batal {user_id}")]
        ]
        pesan = await client.ask(
            user_id,
            f"Silakan kirim pertanyaan Anda.",
            reply_markup=InlineKeyboardMarkup(button),
            timeout=90,
        )
    except asyncio.TimeoutError as out:
        if get.id in SUPPORT:
            SUPPORT.remove(get.id)
            return await client.send_message(get.id, "Pembatalan otomatis karena tidak ada respons.")
    text = f"Pertanyaan Anda sudah terkirim."
    buttons = [
        [
            InlineKeyboardButton("👤 Profil", callback_data=f"profil {user_id}"),
            InlineKeyboardButton("Jawab 💬", callback_data=f"jawab_pesan {user_id}"),
        ],
    ]
    if get.id in SUPPORT:
        try:
            await pesan.copy(
                OWNER_ID,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            SUPPORT.remove(get.id)
            await pesan.request.edit(
                f"Silakan kirim pertanyaan Anda."
            )
            return await client.send_message(user_id, text)
        except Exception as error:
            return await client.send_message(user_id, error)


@PY.CALLBACK("^jawab_pesan")
async def jawab_pesan_callback(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await client.get_users(user_id)
    user_ids = int(callback_query.data.split()[1])
    SUPPORT.append(get.id)
    try:
        button = [
            [InlineKeyboardButton("Batalkan", callback_data=f"batal {user_id}")]
        ]
        pesan = await client.ask(
            user_id,
            f"Silakan kirim balasan Anda.",
            reply_markup=InlineKeyboardMarkup(button),
            timeout=300,
        )
    except asyncio.TimeoutError:
        if get.id in SUPPORT:
            SUPPORT.remove(get.id)
            return await client.send_message(get.id, "Pembatalan otomatis karena tidak ada respons.")
    text = f"Silakan kirim balasan Anda."
    if not user_ids == OWNER_ID:
        buttons = [[InlineKeyboardButton("💬 Jawab 💬", f"jawab_pesan {user_id}")]]
    else:
        buttons = [
            [
                InlineKeyboardButton("👤 Profil", callback_data=f"profil {user_id}"),
                InlineKeyboardButton("Jawab 💬", callback_data=f"jawab_pesan {user_id}"),
            ],
        ]
    if get.id in SUPPORT:
        try:
            await pesan.copy(
                user_ids,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            SUPPORT.remove(get.id)
            await pesan.request.edit(
                f"Silakan kirim balasan Anda.",
            )
            await client.send_message(user_id, text)
        except Exception as error:
            return await client.send_message(user_id, error)


@PY.CALLBACK("^profil")
async def profil_callback(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    try:
        get = await client.get_users(user_id)
        first_name = f"{get.first_name}"
        last_name = f"{get.last_name}"
        full_name = f"{get.first_name} {get.last_name or ''}"
        username = f"{get.username}"
        msg = (
    f"🧑 <a href=tg://user?id={get.id}>{full_name}</a>\n"
    f"📌 ID Pengguna: <code>{get.id}</code>\n"
    f"📛 Nama Depan: {first_name}\n"
)
        if last_name == "None":
            msg += ""
        else:
            msg += f"📛 Nama Belakang: {last_name}\n"
        if username == "None":
            msg += ""
        else:
            msg += f"👤 Username: @{username}\n"
            msg += f"🤖 Bot: {client.me.mention}\n"
        buttons = [
            [
                InlineKeyboardButton(
                    f"{full_name}",
                    url=f"tg://openmessage?user_id={get.id}",
                )
            ]
        ]
        await callback_query.message.reply_text(
            msg, reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as why:
        await callback_query.message.reply_text(why)


@PY.CALLBACK("^batal")
async def batal_callback(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    if user_id in SUPPORT:
        try:
            SUPPORT.remove(user_id)
            await callback_query.message.delete()
            buttons = BTN.START(callback_query)
            return await client.send_message(
                user_id,
                MSG.START(callback_query),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except Exception as why:
            await callback_query.message.delete()
            await client.send_message(user_id, f"❌ Gagal dibatalkan.")
