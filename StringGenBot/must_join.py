from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/TEAM_DST" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph//file/4ced7e4a672638ac5c75e.jpg", caption=f"» 𝐅𝐈𝐑𝐒𝐓 𝐘𝐎𝐔 𝐍𝐄𝐄𝐃 𝐓𝐎 𝐉𝐎𝐈𝐍 𝐎𝐔𝐑 𝐅𝐀𝐌𝐈𝐋𝐘 𝐓𝐇𝐄𝐍 𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐌𝐄 [𝐎𝐅𝐅𝐈𝐂𝐄]({TEAM_DST}). 𝐀𝐅𝐓𝐄𝐑 𝐉𝐎𝐈𝐍 𝐒𝐓𝐀𝐑𝐓 𝐌𝐄 𝐀𝐆𝐀𝐈𝐍 !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("</> 𝐎𝐅𝐅𝐈𝐂𝐄", url=https://t.me/MADARA_WORLD),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MADARA_WORLD} !")
