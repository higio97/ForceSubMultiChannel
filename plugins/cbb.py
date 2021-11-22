#(©)Codexbotz

from pyrogram import __version__
from pyrogram import Client
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🥷 ᴘᴇᴍʙᴜᴀᴛ : <a href='tg://user?id={OWNER_ID}'>ᴏʀᴀɴɢ ɪɴɪ</a>\n🔗 ᴄʜᴀɴɴᴇʟ 𝟷 : <a href='{client.invitelink}'>ᴅɪsɪɴɪ</a>\n🔗 ᴄʜᴀɴɴᴇʟ 2 : <a href='{client.invitelink2}'>ᴅɪsɪɴɪ</a>\n🔗 ᴄʜᴀɴɴᴇʟ 3 : <a href='{client.invitelink3}'>ᴅɪsɪɴɪ</a>\n🔗 ᴄʜᴀɴɴᴇʟ 4 : <a href='{client.invitelink4}'>ᴅɪsɪɴɪ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 𝘿𝙤𝙣𝙖𝙨𝙞 𝘽𝙤𝙩", url='t.me/DonasiNZIDBot')
                    ],
                    [
                        InlineKeyboardButton("🤖 𝙊𝙧𝙙𝙚𝙧 𝙑𝘾𝙎", url='t.me/AdmNZIDBOT')
                    ],
                    [
                        InlineKeyboardButton("🔒 ᴛᴜᴛᴜᴘ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
