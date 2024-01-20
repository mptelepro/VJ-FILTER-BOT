import telebot
import requests
from telebot import types
# Change this BOT Token. You can get it from @BotFather
BOT_TOKEN = "2108094040:AAHY_MkFF5X5HhW4yaZzq49jduK2fySPlhM"

bot = telebot.TeleBot(BOT_TOKEN)




@bot.message_handler(commands=["reverse"])
def reverse_image(message):
    try:
        if message.reply_to_message.content_type == "photo":
            image_file_id = message.reply_to_message.photo[-1].file_id
            file_info = bot.get_file(image_file_id)
            reverse_final_url = requests.get(
                "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                % (bot_token, file_info.file_path)
            ).url
            reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
            bot.send_message(
                message.chat.id,
                "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                reply_markup=types.InlineKeyboardMarkup(
                    [
                        [
                            types.InlineKeyboardButton(
                                text="Search Results", url=reverse_final_url
                            )
                        ],
                        [
                            types.InlineKeyboardButton(
                                text="Kronos Support", url="https://t.me/KeevChat"
                            )
                        ],
                    ]
                ),
            )
        elif message.reply_to_message.content_type == "sticker":
            sticker_file_id = message.reply_to_message.sticker.thumb.file_id
            file_info = bot.get_file(sticker_file_id)
            reverse_final_url = requests.get(
                "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                % (bot_token, file_info.file_path)
            ).url
            reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
            bot.send_message(
                message.chat.id,
                "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                reply_markup=types.InlineKeyboardMarkup(
                    [
                        [
                            types.InlineKeyboardButton(
                                text="Search Results", url=reverse_final_url
                            )
                        ],
                        [
                            types.InlineKeyboardButton(
                                text="Kronos Support", url="https://t.me/KeevChat"
                            )
                        ],
                    ]
                ),
            )
        elif message.reply_to_message.content_type == "video":
            try:
                video_file_id = message.reply_to_message.video.thumb.file_id
                file_info = bot.get_file(video_file_id)
                reverse_final_url = requests.get(
                    "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                    % (bot_token, file_info.file_path)
                ).url
                reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
                bot.send_message(
                    message.chat.id,
                    "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                    reply_markup=types.InlineKeyboardMarkup(
                        [
                            [
                                types.InlineKeyboardButton(
                                    text="Search Results", url=reverse_final_url
                                )
                            ],
                            [
                                types.InlineKeyboardButton(
                                    text="Kronos Support", url="https://t.me/KeevChat"
                                )
                            ],
                        ]
                    ),
                )
            except:
                bot.send_message(message.chat.id, "Unsupported File.")
        elif message.reply_to_message.content_type == "animation":
            try:
                animation_file_id = message.reply_to_message.animation.thumb.file_id
                file_info = bot.get_file(animation_file_id)
                reverse_final_url = requests.get(
                    "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                    % (bot_token, file_info.file_path)
                ).url
                reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
                bot.send_message(
                    message.chat.id,
                    "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                    reply_markup=types.InlineKeyboardMarkup(
                        [
                            [
                                types.InlineKeyboardButton(
                                    text="Search Results", url=reverse_final_url
                                )
                            ],
                            [
                                types.InlineKeyboardButton(
                                    text="Kronos Support", url="https://t.me/KeevChat"
                                )
                            ],
                        ]
                    ),
                )
            except:
                bot.send_message(
                    message.chat.id,
                    "Reverse Image Search is not possible for GIFs sent through Telegram GIF section. Try downloading and send again to reverse search. \nErr: Telegram API Limit",
                )
        else:
            bot.send_message(
                message.chat.id,
                "Reverse Image Search is not possible for this file type. \nErr: File Type Not Supported",
            )
    except:
        bot.send_message(
            message.chat.id,
            "Reply to some image, video, GIF or Sticker to reverse image search.",
        )


@bot.message_handler(commands=["reverse_image_search"])


@bot.message_handler(content_types=["photo","sticker","animation","video"]=commands=["rvs"])
def reverse_image(message):
    if message.chat.type == "private":
        try:
            if message.content_type == "photo":
                image_file_id = message.photo[-1].file_id
                file_info = bot.get_file(image_file_id)
                reverse_final_url = requests.get(
                    "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                    % (bot_token, file_info.file_path)
                ).url
                reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
                bot.send_message(
                    message.chat.id,
                    "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                    reply_markup=types.InlineKeyboardMarkup(
                        [
                            [
                                types.InlineKeyboardButton(
                                    text="Search Results", url=reverse_final_url
                                )
                            ],
                            [
                                types.InlineKeyboardButton(
                                    text="Kronos Support", url="https://t.me/KeevChat"
                                )
                            ],
                        ]
                    ),
                )
            elif message.content_type == "sticker":
                sticker_file_id = message.sticker.thumb.file_id
                file_info = bot.get_file(sticker_file_id)
                reverse_final_url = requests.get(
                    "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                    % (bot_token, file_info.file_path)
                ).url
                reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
                bot.send_message(
                    message.chat.id,
                    "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                    reply_markup=types.InlineKeyboardMarkup(
                        [
                            [
                                types.InlineKeyboardButton(
                                    text="Search Results", url=reverse_final_url
                                )
                            ],
                            [
                                types.InlineKeyboardButton(
                                    text="Kronos Support", url="https://t.me/KeevChat"
                                )
                            ],
                        ]
                    ),
                )
            elif message.reply_to_message.content_type == "video":
                video_file_id = message.reply_to_message.video.thumb.file_id
                file_info = bot.get_file(video_file_id)
                reverse_final_url = requests.get(
                    "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                    % (bot_token, file_info.file_path)
                ).url
                reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
                bot.send_message(
                    message.chat.id,
                    "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                    reply_markup=types.InlineKeyboardMarkup(
                        [
                            [
                                types.InlineKeyboardButton(
                                    text="Search Results", url=reverse_final_url
                                )
                            ],
                            [
                                types.InlineKeyboardButton(
                                    text="Kronos Support", url="https://t.me/KeevChat"
                                )
                            ],
                        ]
                    ),
                )
            elif message.reply_to_message.content_type == "animation":
                try:
                    animation_file_id = message.reply_to_message.animation.thumb.file_id
                    file_info = bot.get_file(animation_file_id)
                    reverse_final_url = requests.get(
                        "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                        % (bot_token, file_info.file_path)
                    ).url
                    reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
                    bot.send_message(
                        message.chat.id,
                        "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                        reply_markup=types.InlineKeyboardMarkup(
                            [
                                [
                                    types.InlineKeyboardButton(
                                        text="Search Results", url=reverse_final_url
                                    )
                                ],
                                [
                                    types.InlineKeyboardButton(
                                        text="Kronos Support", url="https://t.me/KeevChat"
                                    )
                                ],
                            ]
                        ),
                    )
                except:
                    bot.send_message(message.chat.id, "Reverse Image Search is not possible for GIFs sent through Telegram GIF section. Try downloading and send again to reverse search. \nErr: Telegram API Limit")
        except:
            bot.send_message(message.chat.id, "Reverse Image Search is not possible for GIFs sent through Telegram GIF section. Try downloading and send again to reverse search. \nErr: Telegram API Limit")

bot.polling(none_stop=True)
