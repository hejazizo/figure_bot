# -*- coding: UTF-8 -*-
from var_lib import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib
import re
import numpy as np

bot = telebot.TeleBot(token="258999978:AAGmM7bDUDpmMjmgcwkLFI90wKKly8yLez4")


#### WELCOME MESSAGE
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.reply_to(message, "Hi! How are you today?")
        if message.from_user.username in ['Ali_H93']:
            bot.send_message(message.chat.id, "Hi ADMIIIIIIN! 😃")
    except:
        bot.reply_to(message, 'Something went wrong!')


#### STICKERS
@bot.message_handler(content_types=['sticker'])
def handle_text_doc(message):
    # bot.reply_to(message, "Stickers are banned!")
    try:
        if message.from_user.username in ['witcher_mfem']:

            print('counter: ', last_message['counter'])
            print('elapsed: ', message.date - last_message['time'])

            if message.date - last_message['time'] < delay:
                if last_message['counter'] > 0:
                    bot.delete_message(message.chat.id, message.message_id)
                else:
                    last_message['counter'] += 1
            else:
                last_message['counter'] = 0

            last_message['time'] = message.date

        print(message.from_user)
    except:
        bot.reply_to(message, 'Something went wrong!')


#### GIF
@bot.message_handler(content_types=['document'])
def handle_text_doc(message):
    try:
        if message.from_user.username in ['witcher_mfem']:

            if message.document.mime_type == 'video/mp4':

                print('counter: ', last_message['counter'])
                print('elapsed: ', message.date - last_message['time'])

                if message.date - last_message['time'] < delay:
                    if last_message['counter'] > 0:
                        bot.delete_message(message.chat.id, message.message_id)
                    else:
                        last_message['counter'] += 1
                else:
                    last_message['counter'] = 0

                last_message['time'] = message.date

        print(message.from_user)
    except:
        bot.reply_to(message, 'Something Went Wrong!')


#### Diagram
@bot.message_handler(regexp="y *= *.+")
def handle_message(message):
    try:
        pattern = re.search("y *= *(.+)", message.text)
        res = pattern
        print(res.groups()[0])

        bot.reply_to(message, 'found a formula')

        fig = plt.figure()

        # sin() function plot
        ax_s = fig.add_axes([0, 0, 1, 1])
        ax_s.set_frame_on(False)
        x = np.linspace(0, 2 * np.pi, 200)
        ax_s.plot(x, eval(res.groups()[0]), 'r', lw=2, mew=0)

        # plt.show()
        fig.savefig('pic.png')  # save the picture in png format
        photo = open('pic.png', 'rb')
        bot.send_photo(message.chat.id, photo, 'Figure')

        print(message.caption)
        print('User info: ', message.from_user)
    except:
        bot.reply_to(message, 'Something Went Wrong!')


#### ANY MESSAGE
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    pass


#### MAIN
bot.skip_pending = True
bot.polling(none_stop=True, interval=0)
