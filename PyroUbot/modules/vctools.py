__MODULE__ = "ᴠᴄᴛᴏᴏʟꜱ"
__HELP__ = """
**Bantuan Untuk VcTools**

**Perintah:**
- **{0}jvc**  
  **Penjelasan:** Untuk bergabung ke voice chat group.

- **{0}lvc**  
  **Penjelasan:** Untuk meninggalkan voice chat group.
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from asyncio import get_event_loop
from functools import partial
from yt_dlp import YoutubeDL
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from pytgcalls.types.calls import Call
from pyrogram.errors import ChatAdminRequired, UserBannedInChannel
from pytgcalls.exceptions import NotInCallError
from youtubesearchpython import VideosSearch
import os
import wget
import math
from datetime import timedelta
from time import time
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch
from pyrogram.enums import ChatType
from PyroUbot import *

@PY.UBOT("lvc")
@PY.TOP_CMD
@PY.GROUP
async def leave_vc(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    try:
        mex = await message.reply(f"{prs} Sedang diproses...")
        await client.call_py.leave_call(message.chat.id)
        await mex.edit(f"{brhsl} Berhasil turun dari obrolan suara.")
    except NotInCallError:
        await mex.edit(f"{ggl} Belum bergabung ke voice chat.")
    except UserBannedInChannel:
        pass
    except Exception as e:
        print(e)

@PY.UBOT("jvc")
@PY.TOP_CMD
@PY.GROUP
async def join_vc(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    try:
        mex = await message.reply(f"{prs}proccesing...")
        await client.call_py.play(message.chat.id)
        await client.call_py.mute_stream(message.chat.id)
        await mex.edit(f"{brhsl} Berhasil join ke voice chat.")        
    except ChatAdminRequired:
        await mex.edit(f"{ggl} Tidak bisa join vc.")
    except UserBannedInChannel:
        pass
    except Exception as e:
        print(e)
