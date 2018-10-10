# -*- coding: utf-8 -*-

import telebot
import random
import os

TOKEN = '546137272:AAGRdusSVjyKInU9DwH_5JyEbUHH5vHEc10'

bot = telebot.TeleBot(TOKEN)

welcome_text = "Царь позвал к себе Иванушку-дурака и говорит:\n"\
                      "– Если завтра не принесешь двух говорящих птиц – голову срублю.\n"\
                      'Иван принес филина и воробья. Царь говорит:\n'\
                      '– Ну, пусть что-нибудь скажут.\n'\
                      'Иван спрашивает:\n'\
                      '– Воробей, почем раньше водка в магазине была?\n'\
                      'Воробей:\n'\
                      '– Чирик.\n'\
                      'Иван филину:\n'\
                      '– А ты, филин, подтверди.\n'\
                      'Филин:\n'\
                      '– Подтверждаю.'\

help_text = "/start - Стартовая страница \n"\
                "/help - Помощь \n"\
                "/other "

confirmation = ['подтверди', 'подтверждение', 'точно', 'прав']
answer = ['угу', 'подтверждаю', 'точно, точно', 'вы правы', 'неа', 'нет', 'не может быть']


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, help_text)

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
     file_info = bot.get_file(message.sticker.file_id)
     downloaded_file = bot.download_file(file_info.file_path)
     src='d:/222/tmp/'+file_info.file_path;
     with open(src, 'wb') as new_file:
         new_file.write(downloaded_file)
     try:
         bot.send_photo(546137272, downloaded_file)
         file_id = 'AAAaaaZZZzzz'
         bot.send_photo(546137272, file_id)
     except Exception:
         pass
         


@bot.message_handler(func=lambda message: True)
def upper(message):
    seek = False
    for conf in confirmation:
        if conf.upper() in message.text.upper():
            seek = True
    if seek:
        ans = answer[random.randint(0, len(answer)-1)]
        bot.reply_to(message, ans)
    else:
        if random.randint(0,3) == 0 :
            bot.reply_to(message, ' Угу')


bot.polling()