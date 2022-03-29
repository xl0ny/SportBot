import telebot
import traceback
import requests
import schedule
import datetime
import time
from multiprocessing import *

TOKEN = ""

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    busers = open("data/users.txt").read()

    with open("data/users.txt", "a") as f:
        if str(message.chat.id) not in busers:
            f.write(str(message.chat.id) + "\n")

    bot.send_message(message.chat.id, "Привет, это спорт бот !")


if __name__ == '__main__':
    bot.polling(none_stop=True)
