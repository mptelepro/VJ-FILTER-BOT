import telebot
import requests

import os
import requests
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import BOT_TOKEN
from lazybot import LazyPrincessBot


from pyrogram import Client
from database.ia_filterdb import Media
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from aiohttp import web

from pyrogram import Client
from info import *



load_dotenv()
BOT_TOKEN = '5894671404:AAGCQIb0moTV0n34hLZ0dCBERituyY_deIU'
bot = BOT_TOKEN


# Ganti 'TOKEN_REMOVEBG_API' dengan token API Remove.bg Anda
REMOVEBG_API_KEY = 'MJMoiiatXPHcHgFG3D1Wf2aG'




@Client.on_message(filters.command(["test"]))
async def remove_background(bot, message):
    try:
#        if message.reply_to_message.photo:
        file_id = message.reply_to_message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"

        # Kirim permintaan ke Remove.bg API untuk menghapus background gambar
        response = requests.post('https://api.remove.bg/v1.0/removebg', data={'image_url': file_url}, headers={'X-Api-Key': REMOVEBG_API_KEY})

        if response.status_code == 200:
                # Simpan gambar hasil dan kirimkan ke pengguna
            with open('removed_bg.png', 'wb') as f:
                f.write(response.content)
            await message.reply_document(open('removed_bg.png', 'rb'))
        else:
            await bot.send_message("Maaf, tidak dapat menghapus background gambar.")

    except Exception as e:
        await bot.send_message("An error occurred while processing the image..")



