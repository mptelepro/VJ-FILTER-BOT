import urllib
import json

import telebot
import requests

# Ganti 'TOKEN_BOT_ANDA' dengan token bot Telegram Anda
BOT_TOKEN = '2108094040:AAHY_MkFF5X5HhW4yaZzq49jduK2fySPlhM'
bot = telebot.TeleBot(BOT_TOKEN)

# Ganti 'TOKEN_REMOVEBG_API' dengan token API Remove.bg Anda
REMOVEBG_API_KEY = 'MJMoiiatXPHcHgFG3D1Wf2aG'



@bot.message_handler(commands=['yt'])
def command_youtube(m):
    cid = m.chat.id
    query = m.text[4:]
    # sustituir CLAVE API por tu API    
    link = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&q=%s&key={CLAVE API}" % query)
    data = json.loads(link.read())
    """Coge un video aleatorio del primero al tercero,
    este rango se puede modificar o incluso dejar fijo"""
    rnd_no = random.randrange(0,3)
    id = data['items'][rnd_no]['id']['videoId'] 
    bot.send_message(cid, "http://www.youtube.com/watch?v=" + id)

@bot.message_handler(commands=['img'])
def command_img(m):
            cid = m.chat.id
            token = m.text.split(" ", 1)[1]
            token = token.encode('utf-8') 
            url = "https://www.googleapis.com/customsearch/v1?q=%s&cx{CXCODEHERE}&searchType=image&key={APIKEY}" % token
            link = urllib.urlopen(url)
            data = json.loads(link.read())
            rnd_no = random.randrange(0,4)
            image = urllib.URLopener()
            image.retrieve(data['items'][rnd_no]['link'], "tmp.jpg")
            bot.send_photo(cid, open( 'tmp.jpg', 'rb'))



@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"

        # Kirim permintaan ke Remove.bg API untuk menghapus background gambar
        response = requests.post('https://api.remove.bg/v1.0/removebg', data={'image_url': file_url}, headers={'X-Api-Key': REMOVEBG_API_KEY})

        if response.status_code == 200:
            # Simpan gambar hasil dan kirimkan ke pengguna
            with open('removed_bg.png', 'wb') as f:
                f.write(response.content)
            bot.send_document(message.chat.id, open('removed_bg.png', 'rb'))
        else:
            bot.reply_to(message, "Maaf, tidak dapat menghapus background gambar.")

    except Exception as e:
        bot.reply_to(message, "An error occurred while processing the image..")

bot.polling()
