from PyroUbot import *

__MODULE__ = "ɢᴀᴍᴇ"
__HELP__ = """
**Bantuan Untuk Game**

**Perintah:**
- **{0}catur**
    - Digunakan untuk memunculkan game catur.

- **{0}game**
    - Digunakan untuk memunculkan game random.

**Penjelasan:**
- Gunakan perintah **{0}catur** untuk bermain game catur dan tantang kemampuan strategi Anda.
- Dengan perintah **{0}game**, Anda dapat menikmati berbagai game random yang tersedia.

**Notes:** Terdapat lebih dari 500 menu game yang bisa Anda pilih!
"""


@PY.UBOT("catur")
@PY.TOP_CMD
async def _(client, message):
    try:
        x = await client.get_inline_bot_results("GameFactoryBot")
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[0].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)


@PY.UBOT("game")
@PY.TOP_CMD
async def game_cmd(client, message):
    try:
        x = await client.get_inline_bot_results("gamee")
        msg = message.reply_to_message or message
        random_index = random.randint(0, len(x.results) - 1)
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[random_index].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)
