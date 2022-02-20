import telebot
import re

import urlshortener

bot_token = 'token'
bot = telebot.TeleBot(bot_token)
rexpr = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("send "+message.text)
    bot.reply_to(message, 'Welcome to the best Url shortener\nJust send me a link and I\'ll shorten it.')


@bot.message_handler(commands=['urlshortener'])
def send_welcome(message):

    bot.reply_to(message, "Entter url..")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'i can help you manage Telegram bols.\n\nyou can control me by sending these commandd:\n\n'
                          '/start\n'
                          '/urlshortener\n')


@bot.message_handler(regexp=rexpr)
def command_help(message):

    print("send   " + message.text)
    chek = re.findall(rexpr, message.text)
    if chek:
        shorturl = urlshortener.urlshortnerM(message.text)
        bot.reply_to(message, shorturl)
    else:
        bot.reply_to(message, "Please Enter Valid Url")

@bot.message_handler(func=lambda message: True)
def command_handle_document(message):
    bot.send_message(message.chat.id, 'Please enter valid Url')

print("bhautik maru")

bot.polling()
