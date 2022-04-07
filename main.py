import telebot
import traceback
import requests
import schedule
import datetime
import time
from multiprocessing import *

TOKEN = "5059019243:AAHvLlYGSfZudusSa6gpjthnlDbmcXQz_64"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    users = open("data/users.txt").read()

    with open("data/users.txt", "a") as f:
        if str(message.chat.id) not in users:
            f.write(str(message.chat.id) + "\n")

    bot.send_message(message.chat.id, "Привет, это спорт бот !")


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Напишите /matches, чтобы вывести список сегодняшних матчей\n"+
                                      "Напишите /timer {период в часах}, чтобы установить таймер присылания информации\n"+
                                      "Напишите /set_team {команда}, чтобы получать уведомления о любомой команде")


@bot.message_handler(commands=['timer'])
def set_t(message: telebot.types.Message):
    pass


@bot.message_handler(commands=['set_team'])
def unset_t(message: telebot.types.Message):
    pass


def start_process():  # Запуск Process
    p1 = Process(target=Evr.start_schedule(), args=()).start()


class Evr():
    def start_schedule():  # Запуск schedule
        ######Параметры для schedule######
        schedule.every(5).seconds.do(Evr.send_to_all)
        ##################################

        while True:  # Запуск цикла
            schedule.run_pending()
            time.sleep(1)

    def send_to_all():
        for i in open('data/users.txt'):
            bot.send_message(int(i.strip()), "smth")


# while True:
#     schedule.run_pending()
#     time.sleep(1)
if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass

