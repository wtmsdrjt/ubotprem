import importlib
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PyroUbot import bot, ubot
from PyroUbot.core.helpers import PY
from PyroUbot.modules import loadModule
from PyroUbot.core.database import *
from PyroUbot.config import OWNER_ID
from platform import python_version
from pyrogram import __version__
HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = importlib.import_module(f"PyroUbot.modules.{mod}")
        module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
        if module_name:
            HELP_COMMANDS[module_name] = imported_module
    print(f"Bot berhasil diaktifkan!")
    await bot.send_message(OWNER_ID, 
       f"""                    
🤖 <b>{bot.me.mention} telah berhasil diaktifkan!</b>
📁 <b>Modul yang tersedia: {len(HELP_COMMANDS)}</b>
📘 <b>Versi Python: {python_version()}</b>
📙 <b>Versi Pyrogram: {__version__}</b>

👤 <b>Jumlah pengguna bot: {len(ubot._ubot)}</b>
""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🤖 Daftar Pengguna Bot 🤖", callback_data="cek_ubot"),
                ],
            ]
        ),
                          )
    
@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
