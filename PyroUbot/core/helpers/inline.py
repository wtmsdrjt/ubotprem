from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton
from pyrogram.errors import MessageNotModified
from pyrogram.types import *
from pyromod.helpers import ikb
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)
                            
from PyroUbot import *


def detect_url_links(text):
    link_pattern = (
        r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?"
    )
    link_found = re.findall(link_pattern, text)
    return link_found


def detect_button_and_text(text):
    button_matches = re.findall(r"\| ([^|]+) - ([^|]+) \|", text)
    text_matches = (
        re.search(r"(.*?) \|", text, re.DOTALL).group(1) if "|" in text else text
    )
    return button_matches, text_matches


def create_inline_keyboard(text, user_id=False, is_back=False):
    keyboard = []
    button_matches, text_matches = detect_button_and_text(text)

    prev_button_data = None
    for button_text, button_data in button_matches:
        data = (
            button_data.split("#")[0]
            if detect_url_links(button_data.split("#")[0])
            else f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]} {button_data.split('#')[0]}"
        )
        cb_data = data if user_id else button_data.split("#")[0]
        if "#" in button_data:
            if prev_button_data:
                if detect_url_links(cb_data):
                    keyboard[-1].append(InlineKeyboardButton(button_text, url=cb_data))
                else:
                    keyboard[-1].append(
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    )
            else:
                if detect_url_links(cb_data):
                    button_row = [InlineKeyboardButton(button_text, url=cb_data)]
                else:
                    button_row = [
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    ]
                keyboard.append(button_row)
        else:
            if button_data.startswith("http"):
                button_row = [InlineKeyboardButton(button_text, url=cb_data)]
            else:
                button_row = [InlineKeyboardButton(button_text, callback_data=cb_data)]
            keyboard.append(button_row)

        prev_button_data = button_data

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    if user_id and is_back:
        markup.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    "Kembali",
                    f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]}",
                )
            ]
        )

    return markup, text_matches


class BTN:
    def ALIVE(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="Help",
                    callback_data="help_back",
                )
            ]
        ]
        return button

    def BOT_HELP(message):
        button = [
            [InlineKeyboardButton("Restart", callback_data="reboot")],
            [InlineKeyboardButton("System", callback_data="system")],
            [InlineKeyboardButton("Ubot", callback_data="ubot")],
            [InlineKeyboardButton("Update", callback_data="update")],
        ]
        return button
        
    def ADD_EXP(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} Bulan",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "👤 Lihat profil pengguna 👤", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "❌ Tolak Pembayaran ❌", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def EXP_UBOT():
        button = [
            [InlineKeyboardButton("beli userbot", callback_data="bahan")],
        ]
        return button

    
    def START(message):
        if not message.from_user.id == OWNER_ID:
            button = [
                [InlineKeyboardButton("🔥 Beli Userbot 🔥", callback_data="bahan")],
                [
                    InlineKeyboardButton("🏆 Buat Userbot 🏆", callback_data="buat_ubot"),
                    InlineKeyboardButton("📁 Module 📁", callback_data="help_back")
                ],
                [InlineKeyboardButton("💬 Bantuan 💬", callback_data="support")]
            ]
        else:
            button = [
                [InlineKeyboardButton("🔥 Buat Userbot 🔥", callback_data="bahan")],
                [
                    InlineKeyboardButton("🛠️ Gitpull 🛠️", callback_data="cb_gitpull"),
                    InlineKeyboardButton("🔁 Restart 🔁", callback_data="cb_restart")
                ],
                [
                    InlineKeyboardButton("🤖 List Userbot 🤖", callback_data="cek_ubot")
                ]
            ]
        return button

    def PLUS_MINUS(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-1",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+1",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("✅ Konfirmasi", callback_data="confirm")],
            [InlineKeyboardButton("🔙 Batalkan", callback_data=f"home {user_id}")],
        ]
        return button

    
    def UBOT(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "📁 Hapus dari database 📁",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "📲 Dapatkan nomor telepon 📲",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "⏳ Cek masa aktif ⏳",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔑 Dapatkan kode OTP 🔑",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔐 Dapatkan kode 2FA 🔐",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "☠ Hapus akun ☠", callback_data=f"ub_deak {int(count)}"
                )
            ],
            [
                InlineKeyboardButton("⬅️", callback_data=f"p_ub {int(count)}"),
                InlineKeyboardButton("➡️", callback_data=f"n_ub {int(count)}"),
            ],
        ]
        return button

    def DEAK(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "🔙 Kembali",
                    callback_data=f"p_ub {int(count)}"
                ),
                InlineKeyboardButton(
                    "Setujui ✅", callback_data=f"deak_akun {int(count)}",
                ),
            ],
        ]
        return button
    def PLUS_MINUS(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-1",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+1",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("✅ Konfirmasi", callback_data="confirm")],
            [InlineKeyboardButton("🔙 Batalkan", callback_data=f"home {user_id}")],
        ]
        return button

    
    def UBOT(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "📁 Hapus dari database 📁",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "📲 Dapatkan nomor telepon 📲",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "⏳ Cek masa aktif ⏳",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔑 Dapatkan kode OTP 🔑",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔐 Dapatkan kode 2FA 🔐",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "☠ Hapus akun ☠", callback_data=f"ub_deak {int(count)}"
                )
            ],
            [
                InlineKeyboardButton("⬅️", callback_data=f"p_ub {int(count)}"),
                InlineKeyboardButton("➡️", callback_data=f"n_ub {int(count)}"),
            ],
        ]
        return button

    def DEAK(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "🔙 Kembali",
                    callback_data=f"p_ub {int(count)}"
                ),
                InlineKeyboardButton(
                    "Setujui ✅", callback_data=f"deak_akun {int(count)}",
                ),
            ],
        ]
        return button

async def create_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    msg = []
    if "-/" not in m.text.split(None, 1)[1]:
        for X in m.text.split(None, 1)[1].split():
            X_parts = X.split(":", 1)
            keyboard.append(
                InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1])
            )
            msg.append(X_parts[0])
        buttons.add(*keyboard)
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            text = " ".join(msg)
    else:
        for X in m.text.split("-/", 1)[1].split():
            X_parts = X.split(":", 1)
            keyboard.append(
                InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1])
            )
        buttons.add(*keyboard)
        text = m.text.split("-/", 1)[0].split(None, 1)[1]

    return buttons, text


async def notes_create_button(text):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = text.split("-/", 1)
    for X in split_text[1].split():
        split_X = X.split(":", 1)
        button_text = split_X[0].replace("_", " ")
        button_url = split_X[1]
        keyboard.append(InlineKeyboardButton(button_text, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0]
    return buttons, text_button
