from pyrogram import Client ,idle
from plugins.helpers.config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
import wget
from pyrogram import enums
import asyncio
from asyncio import *
import time

USERNAME = "NASRANI_BOT"

@Client.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    m = await message.reply_text("**♻ Creating your Logo ♻**......\n\n[░░░░░░░░░░] 00%")
    
    BOT_USERNAME = USERNAME
    search_term = message.text
    s=f.replace('/logo ' ,'')
    text=s.replace(' ', '%20')
    lol = (f"https://www.google.no/search?q={search_term}&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&safe=active&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982")
    photo = wget.download(lol, 'pythonlogo.png')
    await m.delete()
    caption = f"""
✍️__**Logo**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **@{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[• 𝙊𝙪𝙩𝙧𝙪𝙞𝙓 • ™](https://t.me/TeamOutruix)**
◇───────────────◇️  
"""
    # await _.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)
   # time.sleep(3)
    buttons = [[
        InlineKeyboardButton("•••Telegraph Link•••", url=f"{lol}")
        
    ]]
    await message.reply_photo(
        photo=photo,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
 
                 
