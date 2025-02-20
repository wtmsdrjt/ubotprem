import asyncio
import io
import os

import cv2
import requests
from pyrogram import raw

from PyroUbot import *

async def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": RMBG_API,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )

__MODULE__ = "ʀᴇᴍᴏᴠᴇʙɢ"
__HELP__ = """
**Bantuan Untuk Remove BG**

**Perintah:**
- **{0}rmbg** [reply gambarnya]  

**Penjelasan:** 
- Untuk menghapus latar belakang gambar. Gunakan perintah ini untuk menghilangkan latar belakang dari gambar yang Anda balas, sehingga hanya objek utama yang tersisa.
"""

@PY.UBOT("rmbg")
async def rbg_cmd(client, message):
    if RMBG_API is None:
        return
    if message.reply_to_message:
        reply_message = message.reply_to_message
        xx = await message.reply("Sedang diproses...")
        try:
            if (
                isinstance(reply_message.media, raw.types.MessageMediaPhoto)
                or reply_message.media
            ):
                downloaded_file_name = await client.download_media(
                    reply_message, "./downloads/"
                )
                await xx.edit("Menghapus latar belakang....")
                output_file_name = await ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
            else:
                await xx.edit("❌ Gagal menghapus latar belakang.")
        except Exception as e:
            await xx.edit(f"{(str(e))}")
            return
        contentType = output_file_name.headers.get("content-type")
        if "image" in contentType:
            with io.BytesIO(output_file_name.content) as remove_bg_image:
                remove_bg_image.name = "rbg.png"
                await client.send_document(
                    message.chat.id,
                    document=remove_bg_image,
                    force_document=True,
                    reply_to_message_id=message.id,
                )
                await xx.delete()
        else:
            await xx.edit(
                "❌ Gagal mengakses server.".format(
                    output_file_name.content.decode("UTF-8")
                ),
            )
    else:
        return await message.reply("Mohon reply fotonya.")
