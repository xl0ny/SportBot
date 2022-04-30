import telebot
import traceback
import requests
import schedule
import datetime
import time
from multiprocessing import *
import json
import slezhka
import app
import ast
from math import ceil, floor

TOKEN = "5059019243:AAHvLlYGSfZudusSa6gpjthnlDbmcXQz_64"

bot = telebot.TeleBot(TOKEN)
cntrs = {"Испания": slezhka.spain,
         "Англия": slezhka.england,
         "Бразилия": slezhka.braziliya,
         "Франция": slezhka.france,
         "Голландия": slezhka.gollandia,
         "Италия": slezhka.italia,
         "Португалия": slezhka.portugalia,
         "Швейцария": slezhka.switzerland,
         "Россия": slezhka.russia}


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    with open('data/users.json') as f:
        users = json.load(f)
    if str(message.chat.id) not in users:
        users[str(message.chat.id)] = {"team": [],
                                       "period": "",
                                       "schetchik_novostey": 1,
                                       "last_message": ""}
    with open('data/users.json', 'w') as file:
        json.dump(users, file, ensure_ascii=False)

    um = telebot.types.ReplyKeyboardMarkup(True, True)
    um.row("Коэффиценты сегодня", "Новости", "Подписки")

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
    print(team)
    with open('data/users.json') as f:
        users = json.load(f)
    # print(users)
    users[str(message.chat.id)] = {"team": team,
                                   "period": ""}
    # print(users)
    with open('data/users.json', 'w') as file:
        json.dump(users, file)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    # print(message)
    if str(message.text) == json.load(open('data/users.json'))[str(message.chat.id)][
        "last_message"] and message.text in slezhka.all_teams:
        with open('data/users.json') as f:
            users = json.load(f)
        users[str(message.chat.id)]["schetchik_novostey"] += 1
        with open('data/users.json', 'w') as file:
            json.dump(json.loads(str(users).replace("'", '"')), file)
    else:
        with open('data/users.json') as f:
            users = json.load(f)
        users[str(message.chat.id)]["schetchik_novostey"] = 1
        with open('data/users.json', 'w') as file:
            json.dump(json.loads(str(users).replace("'", '"')), file, skipkeys=False, ensure_ascii=True,
                      check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None,
                      sort_keys=False)
    if message.text == "Коэффиценты сегодня":
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Футбол", "Баскетбол", "Хоккей")
        um.row("/start")
        bot.send_message(message.chat.id, "Выберите вид спорта 🏀⚽️🤾‍️⛹️‍️", reply_markup=um)
    elif message.text == "Новости":
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Испания", "Англия", "Бразилия")
        um.row("Франция", "Голландия", "Италия")
        um.row("Португалия", "Швейцария", "Россия")
        um.row("/start")
        bot.send_message(message.chat.id, "Выбери страну", reply_markup=um)
    elif message.text == "Подписки":
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Мои подписки", "Хочу подписаться")
        um.row("/start")
        bot.send_message(message.chat.id, "Выбери действие", reply_markup=um)
    elif message.text == "Мои подписки":
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Подписки")
        um.row("/start")
        with open('data/users.json') as f:
            users = json.load(f)
            # print(users[str(message.chat.id)]['team'])
            if users[str(message.chat.id)]['team']:
                bot.send_message(message.chat.id, f"Ваши подписки: {', '.join(users[str(message.chat.id)]['team'])}",
                                 reply_markup=um)
            else:
                # print(1)
                bot.send_message(message.chat.id, f"У вас пока нет подписок",
                                 reply_markup=um)
    elif message.text == "Хочу подписаться":
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("⠀Испания", "⠀Англия", "⠀Бразилия")
        um.row("⠀Франция", "⠀Голландия", "⠀Италия")
        um.row("⠀Португалия", "⠀Швейцария", "⠀Россия")
        um.row("/start")
        bot.send_message(message.chat.id, "Выбери страну", reply_markup=um)
    elif message.text.replace('⠀', '') in cntrs and not message.text in cntrs:
        # print('asd')
        # print(list(slezhka.all_teams.keys()))
        cntr_mas = list(cntrs[message.text.replace('⠀', '')])
        print(cntr_mas)
        # print(list(cntrs.items()))
        sup = []
        if len(cntr_mas) == 16:
            flag = 0
            um = telebot.types.ReplyKeyboardMarkup(True, True)
            timusi = [cntr_mas[0], cntr_mas[1], cntr_mas[2], cntr_mas[3],
                      cntr_mas[4], cntr_mas[5], cntr_mas[6], cntr_mas[7],
                      cntr_mas[8], cntr_mas[9], cntr_mas[10], cntr_mas[11],
                      cntr_mas[12], cntr_mas[13], cntr_mas[14], cntr_mas[15]]
            for i in users[''.join(str(message.chat.id))]['team']:
                if i in timusi:
                    timusi.remove(i)
            # print(timusi)
            for i in range(ceil(len(timusi) / 2)):
                if len(timusi) - i > ceil(len(timusi) / 2):
                    print('asd')
                    um.row('⠀' + timusi[flag], '⠀' + timusi[flag + 1])
                    if not len(timusi) - flag < 2:
                        flag += 2
                if len(timusi) - i == ceil(len(timusi) / 2):
                    um.row('⠀' + timusi[-1])
            print(timusi)
            print(sup)
        elif len(cntr_mas) == 10:
            flag = 0
            um = telebot.types.ReplyKeyboardMarkup(True, True)
            timusi = [cntr_mas[0], cntr_mas[1], cntr_mas[2], cntr_mas[3],
                      cntr_mas[4], cntr_mas[5], cntr_mas[6], cntr_mas[7],
                      cntr_mas[8], cntr_mas[9]]
            for i in users[''.join(str(message.chat.id))]['team']:
                if i in timusi:
                    timusi.remove(i)
            for i in range(ceil(len(timusi) / 2)):
                if len(timusi) - i > ceil(len(timusi) / 2):
                    print('asd')
                    um.row('⠀' + timusi[flag], '⠀' + timusi[flag + 1])
                    if not len(timusi) - flag < 2:
                        flag += 2
                if len(timusi) - i == ceil(len(timusi) / 2):
                    um.row('⠀' + timusi[-1])
            print(timusi)

        else:
            flag = 0
            um = telebot.types.ReplyKeyboardMarkup(True, True)
            timusi = [cntr_mas[0], cntr_mas[1], cntr_mas[2]]
            for i in users[''.join(str(message.chat.id))]['team']:
                if i in timusi:
                    timusi.remove(i)
            for i in range(ceil(len(timusi) / 2)):
                if len(timusi) - i > ceil(len(timusi) / 2):
                    print('asd')
                    um.row('⠀' + timusi[flag], '⠀' + timusi[flag + 1])
                    if not len(timusi) - flag < 2:
                        flag += 2
                if len(timusi) - i == ceil(len(timusi) / 2):
                    um.row('⠀' + timusi[-1])
            print(timusi, 'kebab')
        bot.send_message(message.chat.id, "Выбери команду", reply_markup=um)
    elif message.text.replace('⠀', '') in list(slezhka.all_teams.keys()) and not message.text in list(
            slezhka.all_teams.keys()):
        # print('dsa')
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        if not message.text.replace('⠀', '') in users[''.join(str(message.chat.id))]['team']:
            with open('data/users.json') as f:
                users = json.load(f)
            # print(str(message.chat.id))
            # print(users)
            users[''.join(str(message.chat.id))]['team'].append(''.join(str(message.text)).replace('⠀', ''))
        # print(users)
        with open('data/users.json', 'w') as file:
            json.dump(json.loads(str(users).replace("'", '"')), file, ensure_ascii=False)
        um.row("Коэффиценты сегодня", "Новости", "Подписки")
        bot.send_message(message.chat.id, 'Подписка оформлена', reply_markup=um)

    elif message.text in cntrs:
        country = message.text
        cntr_mas = list(cntrs[message.text])
        # print(cntr_mas)
        # print(list(cntrs.items()))
        try:
            um = telebot.types.ReplyKeyboardMarkup(True, False)
            um.row(cntr_mas[0], cntr_mas[1])
            um.row(cntr_mas[2], cntr_mas[3])
            um.row(cntr_mas[4], cntr_mas[5])
            um.row(cntr_mas[6], cntr_mas[7])
            um.row(cntr_mas[8], cntr_mas[9])
            um.row(cntr_mas[10], cntr_mas[11])
            um.row(cntr_mas[12], cntr_mas[13])
            um.row(cntr_mas[14], cntr_mas[15])
            um.row("Новости")
        except Exception:
            try:
                um = telebot.types.ReplyKeyboardMarkup(True, False)
                um.row(cntr_mas[0], cntr_mas[1])
                um.row(cntr_mas[2], cntr_mas[3])
                um.row(cntr_mas[4], cntr_mas[5])
                um.row(cntr_mas[6], cntr_mas[7])
                um.row(cntr_mas[8], cntr_mas[9])
            except Exception:
                um = telebot.types.ReplyKeyboardMarkup(True, False)
                um.row(cntr_mas[0], cntr_mas[1], cntr_mas[2])
        bot.send_message(message.chat.id, "Выбери команду", reply_markup=um)
    elif str(message.text) == json.load(open('data/users.json'))[str(message.chat.id)][
        "last_message"] and message.text in slezhka.all_teams:
        # print('Абдулахмед')
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Коэффиценты сегодня", "Новости", "Подписки")
        x = int(users[str(message.chat.id)]["schetchik_novostey"])
        for i in slezhka.get_news(slezhka.all_teams[message.text])[x + 2:x + 3]:
            bot.send_message(message.chat.id, i)
    elif message.text in slezhka.all_teams:
        # print(1)
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Коэффиценты сегодня", "Новости", "Подписки")
        for i in slezhka.get_news(slezhka.all_teams[message.text])[
                 :int(users[str(message.chat.id)]["schetchik_novostey"]) + 3]:
            bot.send_message(message.chat.id, i)
    elif message.text == "Футбол":
        bot.send_message(message.from_user.id, "Загрузка...")
        for i in app.football():
            print(i)
            bot.send_message(message.from_user.id, i)
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Футбол", "Баскетбол", "Хоккей")
        um.row("/start")
        bot.send_message(message.chat.id, "Все матчи на сегодня выведены !", reply_markup=um)
    else:
        pass

    users[str(message.chat.id)]["last_message"] = str(message.text)
    with open('data/users.json', 'w') as file:
        json.dump(json.loads(str(users).replace("'", '"').replace('⠀', '')), file, ensure_ascii=False)


def start_process():  # Запуск Process
    p1 = Process(target=Evr.start_schedule, args=()).start()


class Evr:

    @staticmethod
    def start_schedule():
        schedule.every(1).hour.do(Evr.send_to_all)

        while True:
            schedule.run_pending()
            time.sleep(1)

    @staticmethod
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
