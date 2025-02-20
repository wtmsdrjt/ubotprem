from PyroUbot import *

__MODULE__ = "ғɪʟᴛᴇʀ"
__HELP__ = """
**Bantuan Untuk Filters**

**Perintah:**
- **{0}pfilter** atau **{0}filter**
    - Digunakan untuk mengaktifkan atau menonaktifkan filters di private chat atau group.

- **{0}paddfilter** atau **{0}addfilter**
    - Digunakan untuk menambahkan filters ke database.

- **{0}pdelfilter** atau **{0}delfilter**
    - Digunakan untuk menghapus filters dari database.

- **{0}pfilters** atau **{0}filters**
    - Digunakan untuk mendapatkan semua daftar filters.

**Penjelasan:**
- Gunakan perintah **{0}pfilter** atau **{0}filter** untuk mengelola filters sesuai kebutuhan Anda.
- Dengan **{0}paddfilter** atau **{0}addfilter**, Anda dapat menambahkan filters baru ke dalam sistem.
- Untuk menghapus filters yang tidak lagi diperlukan, gunakan **{0}pdelfilter** atau **{0}delfilter**.
- Jika Anda ingin melihat semua filters yang tersedia, gunakan **{0}pfilters** atau **{0}filters**.

**Note:** Perintah ini hanya berlaku untuk chat pribadi dan sebaliknya.
"""
@PY.NO_CMD_UBOT("FILTER_MSG", ubot)
async def _(client, message):
    try:
        chat_logs = client.me.id
        all_filters = await all_vars(client.me.id, "FILTERS") or {}
        
        for key, value in all_filters.items():
            if key == message.text.split()[0]:
                msg = await client.get_messages(int(chat_logs), int(value))
                return await msg.copy(message.chat.id, reply_to_message_id=message.id)
    except BaseException:
        pass

@PY.UBOT("filter")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs} Sedang diproses...")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"{ggl} Mohon berikan input on/off")

    type = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "FILTER_ON_OFF", type)
    return await txt.edit(f"{sks} Filters berhasil disetting ke {type}.")


@PY.UBOT("addfilter")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs} Sedang diproses...")
    type, reply = extract_type_and_msg(message)

    if not type and message.reply_to_message:
        return await txt.edit(f"{ggl} Harap balas pesan dan berikan nama.")

    logs = client.me.id
    if bool(logs):
        try:
            msg = await reply.copy(int(logs))
            await set_vars(client.me.id, type, msg.id, "FILTERS")
            await txt.edit(f"{sks} Filters {type} berhasil disimpan.")
        except Exception as error:
            await txt.edit(error)
    else:
        return await txt.edit(f"{ggl} Tidak dapat membuat filters baru.")


@PY.UBOT("delfilter")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs} Sedang diproses...")
    arg = get_arg(message)

    if not arg:
        return await txt.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>nama_filter</b>")

    logs = client.me.id
    all = await all_vars(client.me.id, "FILTERS")

    if arg not in all:
        return await txt.edit(f"{ggl} Filter {arg} tidak ditemukan.")

    await remove_vars(client.me.id, arg, "FILTERS")
    await client.delete_messages(logs, all[arg])
    return await txt.edit(f"{sks} Filter {arg} berhasil dihapus.")


@PY.UBOT("filters")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    vars = await all_vars(client.me.id, "FILTERS")
    if vars:
        msg = "<emoji id=5411165185253592513>📝</emoji> **Daftar Filter**\n"
        for x in vars.keys():
            msg += f"├<emoji id=5316946234278169031>⏩</emoji> {x}\n"
        msg += f"• Total filter: {len(vars)}"
    else:
        msg = "<emoji id=6114014038960638990>❌</emoji> Tidak ada filters yang tersimpan."

    return await message.reply(msg, quote=True)
