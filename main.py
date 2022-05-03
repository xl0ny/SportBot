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
import pymorphy2

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
photos = {'https://sportotvet.ru/wp-content/uploads/2018/12/winline-1.png': 'Winline',
          'https://static.legalcdn.org/35/30/60866f3b22a37_1619423035-392x392.png': 'Olimpbet',
          'https://ratingbet.com/upload/bookmaker/image_64.jpg': '1XСТАВКА',
          'https://s5o.ru/storage/dumpster/8/0b/17cd842b9c7cf0b57dc0058b667fe.png': 'МЕЛБЕТ',
          'https://s5o.ru/storage/dumpster/c/03/b24638d8c4acd2fa7fdeb100719ad.png': 'PINNACLE',
          'https://s5o.ru/storage/dumpster/4/c3/cfa1c3c8e37f1d29e966a3e2ccf76.png': 'FONBET',
          'https://tennis-gambling.com/wp-content/uploads/2020/05/p1.jpg': 'LEON',
          'https://milanac.ru/wp-content/uploads/2022/01/becity.png': 'БЕТСИТИ',
          'http://tennisi.bet/Images/top/top_tennisi_tbet3.png': 'TENNISI bet',
          'https://arbers.ru/wp-content/uploads/2017/04/marathonbet.png': 'МАРАФОН bet',
          'https://s5o.ru/storage/dumpster/c/c2/78ac4bd08ba8322a2b5fd13d1602f.png': 'Лига ставок'
          }

links = {'https://winline.ru': 'Winline',
         'https://www.olimp.bet': 'Olimpbet',
         'https://1xstavka.ru': '1XСТАВКА',
         'https://melbet.ru': 'МЕЛБЕТ',
         'https://www.pinnacle.com': 'PINNACLE',
         'https://www.fon.bet': 'FONBET',
         'https://leon.ru': 'LEON',
         'https://betcity.ru': 'БЕТСИТИ',
         'https://tennisi.bet': 'TENNISI bet',
         'https://www.marathonbet.ru/su/betting/Football+-+11': 'МАРАФОН bet',
         'https://www.ligastavok.ru/?utm_referrer=https%3A%2F%2Fwww.google.com%2F': 'Лига ставок'
         }

mas_kontor = photos
mas_kontor = {mas_kontor[i]: i for i in mas_kontor}
links = {links[i]: i for i in links}


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    with open('data/users.json') as f:
        users = json.load(f)
    if str(message.chat.id) not in users:
        users[str(message.chat.id)] = {"team": [],
                                       "period": "1",
                                       "schetchik_novostey": 1,
                                       "last_message": "",
                                       "last_sent_time": ""}
    with open('data/users.json', 'w') as file:
        json.dump(users, file, ensure_ascii=False)

    um = telebot.types.ReplyKeyboardMarkup(True, True)
    um.row("Коэффиценты сегодня", "Новости", "Подписки")
    um.row("Обcуждение матча", "Наши букмекеры")

    bot.send_message(message.chat.id, "Привет, это спорт бот !", reply_markup=um)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id,
                     "Напишите /timer {период в часах}, чтобы установить таймер отправки ", "информации\n")


@bot.message_handler(commands=['timer'])
def set_timer(message: telebot.types.Message):
    period = str(message.text)[6:]
    print(period)
    with open('data/users.json') as f:
        users = json.load(f)
    # print(users)
    users[str(message.chat.id)]["period"] = period
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
    # if str(message.chat.id) not in json.load(open('data/users.json')):
    #     with open('data/users.json') as f:
    #         users = json.load(f)
    #     users[str(message.chat.id)] = {"team": [],
    #                                    "period": "",
    #                                    "schetchik_novostey": 1,
    #                                    "last_message": ""}
    #     with open('data/users.json', 'w') as file:
    #         json.dump(users, file, ensure_ascii=False)
    if message.text == "Коэффиценты сегодня":
        print("frfrefnerf")
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Футбол", "Баскетбол", "Хоккей")
        um.row("/start")
        bot.send_message(message.chat.id, "Выберите вид спорта", reply_markup=um)
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
        um.row("Периодичность")
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
    elif message.text == "Периодичность" and json.load(open('data/users.json'))[str(message.chat.id)]["last_sent_time"]:
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        x = ['1', '3', '7']
        x.remove(str(json.load(open('data/users.json'))[str(message.chat.id)]["period"]))
        print(x)
        for i in x:
            um.row(
                f"Раз в {i.replace('1', '')} {str(pymorphy2.MorphAnalyzer().parse('день')[0].make_agree_with_number(int(i)).word)}")
        um.row(
            f"Оставить текущее (Раз в {str(json.load(open('data/users.json'))[str(message.chat.id)]['period']).replace('1', '')} {str(pymorphy2.MorphAnalyzer().parse('день')[0].make_agree_with_number(int(str(json.load(open('data/users.json'))[str(message.chat.id)]['period']))).word)})")
        um.row("/start")
        bot.send_message(message.chat.id, "Выбери периодичность прихода новостей", reply_markup=um)
    elif message.text in ['Раз в 3 дня', 'Раз в 7 дней', 'Раз в  день'] and json.load(open('data/users.json'))[str(message.chat.id)]["last_message"] == 'Периодичность':
        # print('барабан')
        noww = time.strftime("%M %H %d %m %Y", time.localtime())
        nowww = []
        now = ' '
        for i in noww.split():
            if not i[0] == '0':
                nowww.append(i)
            else:
                nowww.append(i[1:])
        now = now.join([i for i in nowww])
        with open('data/users.json') as f:
            users = json.load(f)
        users[''.join(str(message.chat.id))]["last_sent_time"] = now
        # print(type(message.text.split()[-2]))
        if not str(message.text.split()[-2]).isdigit():
            users[''.join(str(message.chat.id))]["period"] = "1"
        else:
            users[''.join(str(message.chat.id))]["period"] = str(message.text.split()[-2])
        # print(users)
        with open('data/users.json', 'w') as file:
            json.dump(json.loads(str(users).replace("'", '"')), file)
        print('барабашка')
        # start_process()

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
        if not json.load(open('data/users.json'))[str(message.chat.id)]["last_sent_time"]:
            noww = time.strftime("%M %H %d %m %Y", time.localtime())
            nowww = []
            now = ' '
            for i in noww.split():
                if not i[0] == '0':
                    nowww.append(i)
                else:
                    nowww.append(i[1:])
            now = now.join([i for i in nowww])
            with open('data/users.json') as f:
                users = json.load(f)
            users[''.join(str(message.chat.id))]["last_sent_time"] = now
            with open('data/users.json', 'w') as file:
                json.dump(json.loads(str(users).replace("'", '"')), file)
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
        um.row("Обcуждение матча", "Наши букмекеры")
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
        um.row("Новости")
        bot.send_message(message.chat.id, "Выбери команду", reply_markup=um)
    elif str(message.text) == json.load(open('data/users.json'))[str(message.chat.id)][
        "last_message"] and message.text in slezhka.all_teams:
        # print('Абдулахмед')
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Коэффиценты сегодня", "Новости", "Подписки")
        um.row("Обcуждение матча", "Наши букмекеры")
        x = int(users[str(message.chat.id)]["schetchik_novostey"])
        for i in slezhka.get_news(slezhka.all_teams[message.text])[x + 2:x + 3]:
            bot.send_message(message.chat.id, i)
    elif message.text in slezhka.all_teams:
        # print(1)
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Коэффиценты сегодня", "Новости", "Подписки")
        um.row("Обcуждение матча", "Наши букмекеры")
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
    elif message.text == "Обcуждение матча":
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row("Коэффиценты сегодня", "Новости", "Подписки")
        um.row("Обcуждение матча", "Наши букмекеры")
        bot.send_message(message.chat.id, "Переходи в чат - https://t.me/+0ypQ6GBR53YxYjcy", reply_markup=um)
    elif message.text == "Наши букмекеры":
        komand_kontor = list(mas_kontor.keys())
        um = telebot.types.ReplyKeyboardMarkup(True, True)
        um.row(komand_kontor[0], komand_kontor[1], komand_kontor[2])
        um.row(komand_kontor[3], komand_kontor[4], komand_kontor[5])
        um.row(komand_kontor[6], komand_kontor[7], komand_kontor[8])
        um.row(komand_kontor[9], komand_kontor[10])
        um.row("/start")
        bot.send_message(message.chat.id, "Выбери букмекера", reply_markup=um)
    elif message.text in mas_kontor:
        print(mas_kontor[message.text])
        bot.send_photo(
            message.chat.id,
            mas_kontor[message.text],
            caption=links[message.text]
        )
    else:
        pass
    if all(i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890 ' for i in str(message.text).lower()):
        users[str(message.chat.id)]["last_message"] = str(message.text)
        with open('data/users.json', 'w') as file:
            json.dump(json.loads(str(users).replace("'", '"').replace('⠀', '')), file, ensure_ascii=False)


def start_process():  # Запуск Process
    mas_podpisok = []
    with open('data/users.json') as f:
        users = json.load(f)
        print(users)
    for user_id in users:
        Process(target=Evr.start_schedule, args=(int(users[user_id]['period']), user_id)).start()


class Evr:

    @staticmethod
    def start_schedule(timeee, user_id):
        print(timeee)
        schedule.every(timeee).seconds.do(Evr.send_to, user=user_id)

        while True:
            schedule.run_pending()
            time.sleep(1)

    @staticmethod
    def send_to(user):
        last_sent = json.load(open('data/users.json'))[str(user)]["last_sent_time"]
        for j in json.load(open('data/users.json'))[str(user)]["team"]:
            bot.send_message(int(user), j)
            team = slezhka.all_teams[j]
            # print(slezhka.get_news_since_to(team, last_sent))
            for i in slezhka.get_news_since_to(team, last_sent):
                print(i)
                bot.send_message(int(user), i)
        bot.send_message(int(user), 'smth')
        noww = time.strftime("%M %H %d %m %Y", time.localtime())
        nowww = []
        now = ' '
        for i in noww.split():
            if not i[0] == '0':
                nowww.append(i)
            else:
                nowww.append(i[1:])
        now = now.join([i for i in nowww])
        with open('data/users.json') as f:
            users = json.load(f)
        users[''.join(str(user))]["last_sent_time"] = now
        with open('data/users.json', 'w') as file:
            json.dump(json.loads(str(users).replace("'", '"')), file)


if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass
