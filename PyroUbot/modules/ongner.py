from PyroUbot import *
import os
import json
import asyncio
import psutil
import random
import requests
import re
import platform
import subprocess
import sys
import traceback
import aiohttp
import filetype
import wget
import math

from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from pyrogram.enums import UserStatus
from PyroUbot import *
from pyrogram import *
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
from datetime import timedelta
from time import time
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch
from pyrogram.enums import ChatType
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from datetime import datetime
from gc import get_objects
from time import time
from pyrogram.raw import *
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from bs4 import BeautifulSoup
from io import BytesIO
from pyrogram.errors.exceptions import *
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from httpx import AsyncClient, Timeout
from PyroUbot import *

__MODULE__ = "ᴏɴɢɴᴇʀ"
__HELP__ = """
**Bantuan Untuk Ongner**

**Perintah:**
- **{0}cping**
    - Memeriksa koneksi.

- **{0}caddbl**
    - Menambahkan double.

- **{0}climit**
    - Mengecek limit.

- **{0}calive**
    - Memeriksa status aktif.

- **{0}ken ganteng ga**
    - Menanyakan keadaan.

- **{0}tes on**
    - Mengaktifkan tes.

- **{0}p**
    - Perintah singkat.

- **{0}ok**
    - Menyatakan persetujuan.

- **{0}sip**
    - Menyatakan setuju.

- **{0}love**
    - Menyatakan cinta.

- **{0}haha**
    - Menyatakan tawa.

- **{0}kuda**
    - Perintah khusus.

**Penjelasan:**
- Gunakan perintah-perintah di atas untuk berinteraksi dengan Ongner. Setiap perintah memiliki fungsi tertentu yang dapat membantu Anda dalam penggunaan aplikasi.
"""
    
@PY.INDRI("pada on ga")
async def padaonga(client, message):
    await message.reply(
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n")
    
@PY.INDRI("ken ganteng ga")
async def didingantenkga(client, message):
    await message.reply(
       "ya benar dia sangat ganteng sekali\n\n- dia baik\n- dia manis\n- dia lucu\n- dia imut\n- dia konbrut awsjshsjhsjs\n\nidaman banget lah pokonya😅☝🏻")

@PY.INDRI("tes on")
async def teson(client, message):
    await message.reply(
       "on, dev!")
        
@PY.INDRI("kuda")
async def _(client, message):
    await message.react("🦄")

@PY.INDRI("love")
async def _(client, message):
    await message.react("❤")

@PY.INDRI("sip")
async def _(client, message):
    await message.react("👍")

@PY.INDRI("ok")
async def _(client, message):
    await message.react("👌")

@PY.INDRI("haha")
async def _(client, message):
    await message.react("😹")

@PY.INDRI("p")
async def _(client, message):
    await message.react("👋")

@PY.INDRI("wow")
async def _(client, message):
    await message.react("😨")
