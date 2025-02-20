import os
import json
import asyncio
import psutil
# import speedtest

from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw import *
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PyroUbot import *

@PY.UBOT("ping")
@PY.TOP_CMD
async def _(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    uptime = await get_time((time() - start_time))
    delta_ping_formatted = round((end - start).microseconds / 10000, 2)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    pantek = await STR.PONG(client)
    ngentod = await STR.OWNER(client)
    kontol = await STR.UBOT(client)
    devs = await STR.DEVS(client)
    babi = client.me.is_premium
    
    _ping = f"""
<b>{pong} Ping:</b> {str(delta_ping_formatted).replace('.', ',')} ms
<b>{tion} Owner:</b> <code>{client.me.mention}</code>
<b>{yubot} Userbot:</b> <code>{bot.me.mention}</code>

<b>🔹 Layanan Userbot - 10K/Bulan 🔹</b>
🔹 Hubungi: @iamcheating
"""
    
    await message.reply(_ping)

@PY.INDRI("1ping")
async def _(client, message):
    command = message.text.split()
    if len(command) < 2:
        return
    
    haku = command[1].replace("@", "")
    if client.me.username != haku:
        return
    
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping_formatted = round((end - start).microseconds / 10000, 2)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    
    _ping = f"""
<b>{pong} Ping:</b> {str(delta_ping_formatted).replace('.', ',')} ms
<b>{tion} Owner:</b> {client.me.mention}
<b>{yubot} Userbot:</b> {bot.me.mention}

<b>🔹 Layanan Userbot - 10K/Bulan 🔹</b>
🔹 Hubungi: @iamcheating
"""

    await message.reply(_ping)