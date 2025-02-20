import os
from gc import get_objects

import gtts
from gpytranslate import Translator
from pykeyboard import InlineKeyboard

from PyroUbot import *


__MODULE__ = "ᴛʀᴀɴꜱʟᴀᴛᴇ"
__HELP__ = """
**Bantuan Untuk Translate**

**Perintah:**
- **{0}tr**  
  **Penjelasan:** Menerjemahkan pesan/text.

- **{0}tts**  
  **Penjelasan:** Merubah text menjadi pesan suara sesuai bahasa.

- **{0}setlang**  
  **Penjelasan:** Merubah bahasa translate.
"""


@PY.UBOT("tts")
@PY.TOP_CMD
async def _(client, message):
    TM = await message.reply("Sedang diproses...")
    if message.reply_to_message:
        language = client._translate[client.me.id]
        words_to_say = message.reply_to_message.text or message.reply_to_message.caption
    else:
        if len(message.command) < 2:
            return await TM.edit(f"{message.text} [reply/text]")
        else:
            language = client._translate[client.me.id]
            words_to_say = message.text.split(None, 1)[1]
    speech = gtts.gTTS(words_to_say, lang=language)
    speech.save("text_to_speech.oog")
    rep = message.reply_to_message or message
    try:
        await client.send_voice(
            chat_id=message.chat.id,
            voice="text_to_speech.oog",
            reply_to_message_id=rep.id,
        )
        await TM.delete()
    except Exception as error:
        await TM.edit(error)
    try:
        os.remove("text_to_speech.oog")
    except FileNotFoundError:
        pass


@PY.UBOT("tr")
@PY.TOP_CMD
async def _(client, message):
    trans = Translator()
    TM = await message.reply("Sedang diproses...")
    if message.reply_to_message:
        dest = client._translate[client.me.id]
        to_translate = message.reply_to_message.text or message.reply_to_message.caption
        source = await trans.detect(to_translate)
    else:
        if len(message.command) < 2:
            return await message.reply(f"{message.text} [reply/text]")
        else:
            dest = client._translate[client.me.id]
            to_translate = message.text.split(None, 1)[1]
            source = await trans.detect(to_translate)
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = f"{translation.text}"
    rep = message.reply_to_message or message
    await TM.delete()
    await client.send_message(message.chat.id, reply, reply_to_message_id=rep.id)


@PY.UBOT("setlang")
@PY.TOP_CMD
async def _(client, message):
    query = id(message)
    try:
        x = await client.get_inline_bot_results(bot.me.username, f"ubah_bahasa {query}")
        return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        return await message.reply(error)


@PY.INLINE("^ubah_bahasa")
async def _(client, inline_query):
    buttons = InlineKeyboard(row_width=3)
    keyboard = []
    for X in lang_code_translate:
        keyboard.append(
            InlineKeyboardButton(
                Fonts.smallcap(X.lower()),
                callback_data=f"set_bahasa {int(inline_query.query.split()[1])} {X}",
            )
        )
    buttons.add(*keyboard)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get bahasa!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(
                        "Silakan pilih bahasa:"
                    ),
                )
            )
        ],
    )


@PY.CALLBACK("^set_bahasa")
async def _(client, callback_query):
    data = callback_query.data.split()
    try:
        m = [obj for obj in get_objects() if id(obj) == int(data[1])][0]
        m._client._translate[m._client.me.id] = lang_code_translate[data[2]]
        return await callback_query.edit_message_text(
            f"Bahasa berhasil diubah ke Fonts.smallcap(data[2].lower())}."
        )
    except Exception as error:
        return await callback_query.edit_message_text(f"{error}")
