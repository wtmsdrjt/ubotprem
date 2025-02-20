from pyrogram.types import *

from PyroUbot import *

__MODULE__ = "ɴᴏᴛᴇ"
__HELP__ = """
**Bantuan Untuk Catatan**

**Perintah:**
- **{0}addnote [name]**
    - Menyimpan sebuah catatan.

- **{0}addcb [name]**
    - Menyimpan sebuah callback.

- **{0}get [name]**
    - Mendapatkan catatan yang disimpan.

- **{0}delnote [name]**
    - Menghapus catatan yang disimpan.

- **{0}delcb [name]**
    - Menghapus callback yang disimpan.

- **{0}listnote**
    - Melihat daftar catatan yang disimpan.

- **{0}listcb**
    - Melihat daftar callback yang disimpan.

**Penjelasan:**
- Gunakan perintah-perintah di atas untuk mengelola catatan dan callback Anda dengan mudah. Anda dapat menambahkan, menghapus, dan melihat catatan atau callback yang telah disimpan. Ini sangat berguna untuk mengorganisir informasi penting.

**Catatan untuk Tombol:**
- Format: | nama tombol - url/callback |
- Untuk membuat tombol menyamping, gunakan tanda #.
"""


@PY.UBOT("addnote|addcb")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) != 2:
        return await message.reply(f"{ggl} Mohon gunakan {message.text.split()[0]} nama_catatan/nama_callback.")
    args = get_arg(message)
    reply = message.reply_to_message
    query = "notes_cb" if message.command[0] == "addcb" else "notes"

    if not args or not reply:
        return await message.reply(
            f"{message.text.split()[0]} [name] [text/reply]"
        )

    vars = await get_vars(client.me.id, args, query)

    if vars:
        return await message.reply(f"{ggl} Catatan {args} ꜱudah ada.")

    value = None
    type_mapping = {
        "text": reply.text,
        "photo": reply.photo,
        "voice": reply.voice,
        "audio": reply.audio,
        "video": reply.video,
        "animation": reply.animation,
        "sticker": reply.sticker,
    }

    for media_type, media in type_mapping.items():
        if media:
            send = await reply.copy(client.me.id)
            value = {
                "type": media_type,
                "message_id": send.id,
            }
            break

    if value:
        await set_vars(client.me.id, args, value, query)
        return await message.reply(
            f"{brhsl} Catatan {args} berhasil tersimpan."
        )
    else:
        return await message.reply(
            f"{message.text.split()[0]} [name] [text/reply]"
        )


@PY.UBOT("delnote|delcb")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    args = get_arg(message)

    if not args:
        return await message.reply(
            f"{message.text.split()[0]} [name]"
        )

    query = "notes_cb" if message.command[0] == "delcb" else "notes"
    vars = await get_vars(client.me.id, args, query)

    if not vars:
        return await message.reply(f"{ggl} Catatan {args} tidak ditemukan.")

    await remove_vars(client.me.id, args, query)
    await client.delete_messages(client.me.id, int(vars["message_id"]))
    return await message.reply(f"{brhsl} Catatan {args} berhasil dihapus.")


@PY.UBOT("get")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    msg = message.reply_to_message or message
    args = get_arg(message)

    if not args:
        return await message.reply(
            f"{message.text.split()[0]} [name]"
        )

    data = await get_vars(client.me.id, args, "notes")

    if not data:
        return await message.reply(
            f"{ggl} Catatan {args} tidak ditemukan."
        )

    m = await client.get_messages(client.me.id, int(data["message_id"]))

    if data["type"] == "text":
        if matches := re.findall(r"\| ([^|]+) - ([^|]+) \|", m.text):
            try:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_notes {client.me.id} {args}"
                )
                return await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=msg.id,
                )
            except Exception as error:
                await message.reply(error)
        else:
            return await m.copy(message.chat.id, reply_to_message_id=msg.id)
    else:
        return await m.copy(message.chat.id, reply_to_message_id=msg.id)


@PY.UBOT("listnote|listcb")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    query = "notes_cb" if message.command[0] == "listcb" else "notes"
    vars = await all_vars(client.me.id, query)
    if vars:
        msg = f"📋 **Daftar Catatan**\n\n"
        for x, data in vars.items():
            msg += f" {x} |({data['type']})\n"
        msg += f"\n{ktrng} Total catatan: {len(vars)}"
    else:
        msg = f"{ggl} Tidak ada catatan."

    return await message.reply(msg, quote=True)


@PY.INLINE("^get_notes")
async def _(client, inline_query):
    query = inline_query.query.split()
    data = await get_vars(int(query[1]), query[2], "notes")
    item = [x for x in ubot._ubot if int(query[1]) == x.me.id]
    for me in item:
        m = await me.get_messages(int(me.me.id), int(data["message_id"]))
        buttons, text = create_inline_keyboard(m.text, f"{int(query[1])}_{query[2]}")
        return await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                (
                    InlineQueryResultArticle(
                        title="get notes!",
                        reply_markup=buttons,
                        input_message_content=InputTextMessageContent(text),
                    )
                )
            ],
        )


@PY.CALLBACK("_gtnote")
async def _(client, callback_query):
    _, user_id, *query = callback_query.data.split()
    data_key = "notes_cb" if bool(query) else "notes"
    query_eplit = query[0] if bool(query) else user_id.split("_")[1]
    data = await get_vars(int(user_id.split("_")[0]), query_eplit, data_key)
    item = [x for x in ubot._ubot if int(user_id.split("_")[0]) == x.me.id]
    for me in item:
        try:
            m = await me.get_messages(int(me.me.id), int(data["message_id"]))
            buttons, text = create_inline_keyboard(
                m.text, f"{int(user_id.split('_')[0])}_{user_id.split('_')[1]}", bool(query)
            )
            return await callback_query.edit_message_text(text, reply_markup=buttons)

        except TypeError:
            return await callback_query.answer("Maaf, tampaknya ada kesalahan dalam pengisian callback oleh pengguna userbot.", show_alert=True)
