from PyroUbot import *

__MODULE__ = "ᴄᴏɴᴛʀᴏʟ"
__HELP__ = """
**Bantuan Untuk Control**

**Perintah:**
- **{0}prefix**
  - Untuk merubah prefix/handler perintah.

- **{0}creat**
  - Untuk membuat grup atau channel.

- **{0}emoji [query]**
  - Untuk merubah emoji pada tampilan tertentu.

**Query:**
- **{0}pong**
- **{0}owner**
- **{0}ubot**
- **{0}gcast**
- **{0}sukses**
- **{0}gagal**
- **{0}proses**
- **{0}group**
- **{0}catatan**
- **{0}afk**
- **{0}waktu**
- **{0}alasan**

**Penjelasan:**
Gunakan perintah di atas sesuai kebutuhan Anda untuk mengontrol berbagai fungsi dalam aplikasi. Anda dapat mengubah prefix, membuat grup atau channel, serta mengubah emoji yang digunakan dalam tampilan tertentu dengan menambahkan query yang sesuai.
"""


@PY.UBOT("creat")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply(
            f"{message.text} [group/channel] [name/titlee]")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.reply("Sedang diproses...")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "group":
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"✅ Berhaꜱil membuat grup grup: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"✅ Berhaꜱil membuat channel: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )


@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    Tm = await message.reply(f"{prs} Sedang diproses...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"{ggl}{message.text} [simbol]")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "threnone":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"{prefix}" for prefix in ub_prefix)
            return await Tm.edit(f"{brhsl} Prefix telah diubah ke: {parsed_prefix}\nJangan sampai lupa dengan prefix yang baru Anda ganti.")
        except Exception as error:
            return await Tm.edit(str(error))


@PY.UBOT("afk")
@PY.TOP_CMD
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    reason = get_arg(message)
    db_afk = {"time": time(), "reason": reason}
    msg_afk = (
        f"{tion} Sedang AFK
{ktrng} Alasan: {reason}"
        if reason
        else f"{tion} Sedang AFK!"
      )
    await set_vars(client.me.id, "AFK", db_afk)
    return await message.reply(msg_afk)



@PY.NO_CMD_UBOT("AFK", ubot)
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    mng = await EMO.WAKTU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_reason = vars.get("reason")
        afk_runtime = await get_time(time() - afk_time)
        rpk = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        afk_text = (
            f"{tion} Sedang AFK\n{mng} Waktu: {afk_runtime}\n{ktrng} Alasan: {afk_reason}"
            if afk_reason
            else f"""
Hello {rpk}!\nTuan saya sedang AFK selama {afk_runtime}.\nMohon tunggu sebentar!
"""
        )
        return await message.reply(afk_text)


@PY.UBOT("unafk")
@PY.TOP_CMD
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    mng = await EMO.WAKTU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_runtime = await get_time(time() - afk_time)
        afk_text = f"{tion} Kembali Online\n{mng} AFK selama: {afk_runtime}"
        await message.reply(afk_text)
        return await remove_vars(client.me.id, "AFK")


@PY.UBOT("emoji")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        msg = await message.reply(f"{prs} Sedang diproses...", quote=True)

        if not client.me.is_premium:
            return await msg.edit(
                f"{ggl} Mohon beli premium terlebih dahulu."
            )

        if len(message.command) < 3:
            return await msg.edit(f"{ggl} Tolong masukkan query dan valuenya.")

        query_mapping = {
          "pong": "EMOJI_PING",
          "owner": "EMOJI_MENTION",
          "ubot": "EMOJI_USERBOT",
          "proses": "EMOJI_PROSES",
          "gcast": "EMOJI_BROADCAST",
          "sukses": "EMOJI_BERHASIL",
          "gagal": "EMOJI_GAGAL",
          "catatan": "EMOJI_KETERANGAN",
          "group": "EMOJI_GROUP",
          "menunggu": "EMOJI_MENUNGGU",
          "alasan": "EMOJI_ALASAN",
          "waktu": "EMOJI_WAKTU",
          "afk": "EMOJI_AFKA",
        }
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_vars(client.me.id, query_var, emoji_id)
                await msg.edit(
                    f"{brhsl} Emoji berhasil di setting ke: <emoji id={emoji_id}>{value}</emoji>"
                )
            else:
                await msg.edit(f"{ggl} Tidak dapat menemukan emoji premium.")
        else:
            await msg.edit(f"{ggl} Mapping tidak ditemukan.")

    except Exception as error:
        await msg.edit(str(error))

