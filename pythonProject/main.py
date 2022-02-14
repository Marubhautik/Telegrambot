import telebot
import re

import urlshortener

bot_token = '5243368069:AAHbax3Tsn15YG45K4Kv10h9UcWCZJGLI90'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'welcome')


@bot.message_handler(commands=['urlshortener'])
def send_welcome(message):
    bot.reply_to(message, 'Enter url')


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'i can help you manage Telegram bols.\n\n'
                          'you can control me by sending these commandd:\n\n'
                          '/start\n'
                          '/urlshortener\n')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.text)
    chek = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
    if chek:
        shorturl = urlshortener.urlshortnerM(message.text)
        bot.reply_to(message, shorturl)


@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.reply_to(message,'invalid command...')


print("bhautik maru  fgg")

bot.polling()
