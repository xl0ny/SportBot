import telebot
import traceback
import requests
import schedule
import datetime
import time
from multiprocessing import *
import json

TOKEN = "5059019243:AAHvLlYGSfZudusSa6gpjthnlDbmcXQz_64"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    with open('data/users.json') as f:
        users = json.load(f)
    if str(message.chat.id) not in users:
        users[str(message.chat.id)] = {"team": "",
                                       "period": ""}
    with open('data/users.json', 'w') as file:
        json.dump(users, file)

    um = telebot.types.ReplyKeyboardMarkup(True, True)
    um.row("Коэфиценты сегодня", "Новости")

    bot.send_message(message.chat.id, "Привет, это спорт бот !", reply_markup=um)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Напишите /matches, чтобы вывести список сегодняшних матчей\n" +
                     "Напишите /timer {период в часах}, чтобы установить таймер присылания "
                     "информации\n" +
                     "Напишите /set_team {команда}, чтобы получать уведомления о любомой команде")


@bot.message_handler(commands=['timer'])
def set_timer(message: telebot.types.Message):
    pass


@bot.message_handler(commands=['set_team'])
def set_team(message: telebot.types.Message):
    team = str(message.text)[9:]
    with open('data/users.json') as f:
        users = json.load(f)
    print(users)
    users[str(message.chat.id)] = {"team": team,
                                   "period": ""}
    print(users)
    with open('data/users.json', 'w') as file:
        json.dump(users, file)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Коэфиценты сегодня":
        bot.send_message(message.from_user.id, 'На')
    elif message.text == "Новости":
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Испания", "Англия", "Бразилия")
        um.row("Франция", "Голландия", "Италия")
        um.row("Португалия", "Швейцария")

        bot.send_message(message.chat.id, "Привет, это спорт бот !", reply_markup=um)


def start_process():  # Запуск Process
    p1 = Process(target=Evr.start_schedule, args=()).start()


class Evr:
    def start_schedule():
        schedule.every(1).hour.do(Evr.send_to_all)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def send_to_all():
        with open('data/users.json') as f:
            users = json.load(f)
        for i in users:
            bot.send_message(int(i), "smth")


if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass
