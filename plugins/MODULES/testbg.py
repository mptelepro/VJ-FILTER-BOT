import os
import requests
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


load_dotenv()
BOT_TOKEN = '2108094040:AAHY_MkFF5X5HhW4yaZzq49jduK2fySPlhM'
bot = telebot.TeleBot(BOT_TOKEN)

# Ganti 'TOKEN_REMOVEBG_API' dengan token API Remove.bg Anda
REMOVEBG_API_KEY = 'MJMoiiatXPHcHgFG3D1Wf2aG'




@Client.on_message(filters.command(["test"]))
async def remove_background(client, message):
    try:
        file_id = message.reply_to_message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"

        # Kirim permintaan ke Remove.bg API untuk menghapus background gambar
        response = requests.post('https://api.remove.bg/v1.0/removebg', data={'image_url': file_url}, headers={'X-Api-Key': REMOVEBG_API_KEY})

        if response.status_code == 200:
            # Simpan gambar hasil dan kirimkan ke pengguna
            with open('removed_bg.png', 'wb') as f:
                f.write(response.content)
            await client.send_document(chat_id, open('removed_bg.png', 'rb'))
        else:
           await client.send_message(chat_id, "Maaf, tidak dapat menghapus background gambar.")

    except Exception as e:
        await client.send_message(chat_id, "An error occurred while processing the image..")
