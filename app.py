# Импортируем необходимые классы.
import requests
from bs4 import BeautifulSoup
import re
import logging



def class_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


# КОММАНДЫ
def get_teams():
    URL = "https://odds.ru/"
    request = requests.get(URL)


    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='table-tournaments__cell table-tournaments__cell_teams')
    for i in films:
        film = i.find('b')

        print(film.text)


# КТО С КЕМ ИГРАЕТ
def get_mathces():
    URL = "https://odds.ru/"
    request = requests.get(URL)
    # Число-ключ в словаре states —
    # втором параметре ConversationHandler'а.


    # Оно указывает, что дальше на сообщения от этого пользователя
    # должен отвечать обработчик states[1].


    # До этого момента обработчиков текстовых сообщений


    # для этого пользователя не существовало,
    # поэтому текстовые сообщения игнорировались.



    soup = BeautifulSoup(request.text, "html.parser")

    films = soup.findAll('div', class_='table-tournaments__cell table-tourname'
                                       'nts__cell_teams')
    for i in films:
        print(i.text.replace("\n", ""))


def main_component():

    URL = "https://odds.ru/football/"
    request = requests.get(URL)
    # Напишем соответствующие функции.

    # Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.

    soup = BeautifulSoup(request.text, "html.parser")

    films = soup.findAll('div', class_='main-component-tabs home-match-list')
    print(films)


    for i in films:
        film = i.find('b')

        print(film)


def second_component():
    URL = "https://odds.ru/football/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    # Зарегистрируем их в диспетчере рядом

    # с регистрацией обработчиков текстовых сообщений.

    # Первым параметром конструктора CommandHandler я

    # вляется название команды.

    # Определяем функцию-обработчик сообщений.
    # У неё два параметра, сам бот и класс updater, принявший сообщение.



    films = soup.findAll('div', class_='main-component-tabs home-match-list')
    print(films)

    for i in films:
        film = i.find('b')
        print(film)



def chain():
    ids = []
    login, password = '12', 'sasad'


logging.basicConfig(level=logging.INFO)
sessionStorage = {}


def handle_dialog(req, res):
    user_id = req['session']['user_id']


    if req['session']['new']:
        sessionStorage[user_id] = {
            'suggests': [

                "Не хочу.",
                "Не буду.",
                "Отстань!",
            ],
            'elephant': True
        }

        res['response']['text'] = 'Привет! Купи слона!'
        res['response']['buttons'] = get_suggests(user_id)
        return


    if req['request']['original_utterance'].lower() in [

        'ладно',
        'куплю',
        'покупаю',
        'хорошо',
        'я покупаю',
        'я куплю'
    ]:
        if sessionStorage[user_id]['elephant']:
            res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!\n' + \
                                      'https://market.yandex.ru/search?text=слон\тА теперь купи кролика!!!'
            sessionStorage[user_id] = {
                'suggests': [

                    "Не хочу.",

                    "Не буду.",

                    "Отстань!",
                ],
                'elephant': False
            }
            res['response']['buttons'] = get_suggests(user_id)
            return

        else:

            res['response'][
                'text'] = 'Кролика можно найти на Яндекс.Маркете!\nhttps://market.yandex.ru/search?text=кролик'
            res['response']['end_session'] = True
            return

    res['response']['text'] = \
        f"Все говорят '{req['request']['original_utterance']}', а ты купи слона!"
    res['response']['buttons'] = get_suggests(user_id)


def get_suggests(user_id):
    session = sessionStorage[user_id]
    suggests = [
        {'title': suggest, 'hide': True}

        for suggest in session['suggests'][:2]
    ]
    session['suggests'] = session['suggests'][1:]
    sessionStorage[user_id] = session
    if len(suggests) < 2:
        if session['elephant']:
            suggests.append({
                "title": "Ладно",

                "url": "https://market.yandex.ru/search?text=слон",

                "hide": True

            })
        else:
            suggests.append({
                "title": "Ладно",
                "url": "https://market.yandex.ru/search?text=кролик",
                "hide": True
            })

    return suggests


def big_heplper():
    URL = "https://odds.ru/football/"
    request = requests.get(URL)

    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='main-component-tabs home-match-list')
    print(films)
    # if 'время' in msg or 'число' in msg or 'дата' in msg or 'день' in msg:
    #     send_some_msg(id, f"{main(id, True)}")

    # else:

    #     send_some_msg(id, f"{main(id)}")
    for i in films:
        film = i.find('b')
        print(film)


dicktator = {'https://odds.ru/upload/media/default/0001/58/thumb_57363_default_big.svg': 'Winline',
             'https://odds.ru/upload/media/default/0001/58/thumb_57384_default_big.svg': 'Olimpbet',
             'https://odds.ru/upload/media/default/0001/58/thumb_57361_default_big.svg': '1XСТАВКА',
             'https://odds.ru/upload/media/default/0001/58/thumb_57391_default_big.svg': 'МЕЛБЕТ',
             'https://odds.ru/upload/media/default/0001/58/thumb_57387_default_big.svg': 'PINNACLE',
             'https://odds.ru/upload/media/default/0001/58/thumb_57367_default_big.svg': 'FONBET',
             'https://odds.ru/upload/media/default/0001/58/thumb_57369_default_big.svg': 'LEON',
             'https://odds.ru/upload/media/default/0001/58/thumb_57371_default_big.svg': 'БЕТСИТИ',
             'https://odds.ru/upload/media/default/0001/58/thumb_57379_default_big.svg': 'TENNISI bet',
             'https://odds.ru/upload/media/default/0001/58/thumb_57377_default_big.svg': 'МАРАФОН bet',
             'https://odds.ru/upload/media/default/0001/58/thumb_57365_default_big.svg': 'Лига ставок'
             }


def football():
    odin = []
    dva = []
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    tri = []
    main_coefficent = []
    team_one = []
    team_two = []
    URL = "https://odds.ru/football/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='tab-contents')
    sami_kontori_pri_pobede = []
    sami_kontori_pri_nichye = []
    sami_kontori_pri_proigrishe = []
    flag = 0
    flag2 = 0
    flag_dlya_url = 0
    main_flag = 0
    liga = []
    ligaviy_flag = 0
    ligaviy_dicktator = {}
    ligaviy_dicktator_ligi = {}

    # for i in films:
    #     print(i.findAll(class_='table-tournaments__title table-tournaments__title_big'))
    print(films)
    for i in films:

        for j in i.findAll(class_='table-tournaments__title table-tournaments__title_big'):
            liga.append(str(str(j).split('>')[-2])[0:-3])
        for j in i.findAll(class_='table-tournaments__row table-tournaments__row_content table-tournaments__row_bk'):
            # print(j.findAll(class_='table-tournaments__bookmaker-name bookmaker-logo'))
            for z in j.findAll(class_='table-tournaments__bookmaker-name bookmaker-logo'):
               # print(i.find(class_='table-tournaments__title table-tournaments__title_big'))
                # print(z)
                if len(sami_kontori_pri_pobede) == len(sami_kontori_pri_nichye) == len(sami_kontori_pri_proigrishe):
                    sami_kontori_pri_pobede.append(
                        re.split('№;333#|"', str(z).replace('(', '№;333#').replace(')', '№;333#'))[-3])
                elif len(sami_kontori_pri_pobede) > len(sami_kontori_pri_nichye):
                    sami_kontori_pri_nichye.append(
                        re.split('№;333#|"', str(z).replace('(', '№;333#').replace(')', '№;333#'))[-3])
                else:
                    sami_kontori_pri_proigrishe.append(
                        re.split('№;333#|"', str(z).replace('(', '№;333#').replace(')', '№;333#'))[-3])
            for m, z in enumerate(j.findAll(class_='table-tournaments__team-name')):

                main_flag += 1
                if int(str(i).find(liga[ligaviy_flag])) < int(str(i).find(re.split('"|<|>', str(z))[-3])):
                    ligaviy_flag += 1
                    #print(liga[ligaviy_flag])
                if main_flag % 2 == 1:
                    team_one.append(re.split('"|<|>', str(z))[-3])
                else:
                    team_two.append(re.split('"|<|>', str(z))[-3])
        for j in i.findAll(class_='table-tournaments__cell table-tournaments__cell_teams'):
            pass
            # print(j)
        # print(i)
        for j in i.findAll(class_='table-tournaments__bookmaker-mobile'):
            pass
        # print(j)
        for j in i.findAll('b'):
            # print(j)
            flag += 1
            if flag % 2 == 0:
                odin.append(re.split('<|>', str(j))[-3])
            else:
                dva.append(re.split('<|>', str(j))[-3])
        for j in i.findAll(class_='table-tournaments__bookmaker-coefficient'):
            flag2 += 1
            # print(j)
            if flag2 % 2 == 0:
                tri.append(str(re.split('<|>', str(j))[-3]))
                if len(tri) == 3:
                    main_coefficent.append(tri)
                    tri = []
        for j in i.findAll(class_='tab-content tab-content_active'):
            pass
            # print(j.findAll('b'))
    for m, j in enumerate(liga):
        ligaviy_dicktator[str(films).find(j)] = j
        #print(ligaviy_dicktator[str(films).find(j)])
    for i in team_one:
        tima_num = 0
        flyaga = 0
        tima_id = str(films).find(i)
        for j in list(ligaviy_dicktator.keys())[flyaga:]:
            # print(j, tima_id)
            flyaga += 1
            # print(j)
            if j < tima_id:
                tima_num = j
            else:
                if ligaviy_dicktator[tima_num] in ligaviy_dicktator_ligi.keys():
                    ligaviy_dicktator_ligi[ligaviy_dicktator[tima_num]].append(i)
                    break
                else:
                    ligaviy_dicktator_ligi[ligaviy_dicktator[tima_num]] = []
                    ligaviy_dicktator_ligi[ligaviy_dicktator[tima_num]].append(i)
                    break
    # print('Европа. Лига чемпионов УЕФА' in ligaviy_dicktator_ligi, ligaviy_dicktator_ligi)
    said = []
    for i in range(len(team_one)):
        # print(team_one[i])
        pobeda = str(sami_kontori_pri_pobede[i]).replace('"', '').replace("'", "")
        nichya = sami_kontori_pri_nichye[i].replace('"', '').replace("'", "")
        proigrish = sami_kontori_pri_proigrishe[i].replace('"', '').replace("'", "")
        for j in ligaviy_dicktator_ligi:
            if team_one[i] in ligaviy_dicktator_ligi[j]:
                if not j in said:
                    print(j)
                    said.append(j)

        # print(pobeda == 'https://odds.ru/upload/media/default/0001/58/thumb_57363_default_big.svg')
        print(team_one[i] + " : " + team_two[i], main_coefficent[i])

        print(f'Лучшая контора для ставки на {team_one[i]}: {dicktator[pobeda]} ')
        print(f'Лучшая контора для ставки на ничью: {dicktator[nichya]}')
        print(f'Лучшая контора для ставки на {team_two[i]}: {dicktator[proigrish]}\n\n\n\n')

def hockey():
    odin = []
    dva = []
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    tri = []
    main_coefficent = []
    team_one = []
    team_two = []
    URL = "https://odds.ru/hockey/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='tab-contents')
    sami_kontori_pri_pobede = []
    sami_kontori_pri_nichye = []
    sami_kontori_pri_proigrishe = []
    flag = 0
    flag2 = 0
    flag_dlya_url = 0
    main_flag = 0
    liga = []
    ligaviy_flag = 0
    ligaviy_dicktator = {}
    ligaviy_dicktator_ligi = {}

    # for i in films:
    #     print(i.findAll(class_='table-tournaments__title table-tournaments__title_big'))
    for i in films:

        for j in i.findAll(class_='table-tournaments__title table-tournaments__title_big'):
            liga.append(str(str(j).split('>')[-2])[0:-3])
        for j in i.findAll(class_='table-tournaments__row table-tournaments__row_content table-tournaments__row_bk'):
            # print(j.findAll(class_='table-tournaments__bookmaker-name bookmaker-logo'))
            for z in j.findAll(class_='table-tournaments__bookmaker-name bookmaker-logo'):
                # print(i.find(class_='table-tournaments__title table-tournaments__title_big'))
                # print(z)
                if len(sami_kontori_pri_pobede) == len(sami_kontori_pri_nichye) == len(sami_kontori_pri_proigrishe):
                    sami_kontori_pri_pobede.append(
                        re.split('№;333#|"', str(z).replace('(', '№;333#').replace(')', '№;333#'))[-3])
                elif len(sami_kontori_pri_pobede) > len(sami_kontori_pri_nichye):
                    sami_kontori_pri_nichye.append(
                        re.split('№;333#|"', str(z).replace('(', '№;333#').replace(')', '№;333#'))[-3])
                else:
                    sami_kontori_pri_proigrishe.append(
                        re.split('№;333#|"', str(z).replace('(', '№;333#').replace(')', '№;333#'))[-3])
            for m, z in enumerate(j.findAll(class_='table-tournaments__team-name')):
                # print(int(str(i).find(re.split('"|<|>', str(z))[-3])), int(str(i).find(liga[ligaviy_flag])), len(liga))
                main_flag += 1
                if ligaviy_flag + 1 < len(liga):
                    #print(int(str(i).find(liga[ligaviy_flag])) < int(str(i).find(re.split('"|<|>', str(z))[-3])))
                    ligaviy_flag += 1
                # print(liga[ligaviy_flag])

                if main_flag % 2 == 1:
                    team_one.append(re.split('"|<|>', str(z))[-3])
                else:
                    team_two.append(re.split('"|<|>', str(z))[-3])
        for j in i.findAll(class_='table-tournaments__cell table-tournaments__cell_teams'):
            pass
            # print(j)
        # print(i)
        for j in i.findAll(class_='table-tournaments__bookmaker-mobile'):
            pass
        # print(j)
        for j in i.findAll('b'):
            # print(j)
            flag += 1
            if flag % 2 == 0:
                odin.append(re.split('<|>', str(j))[-3])
            else:
                dva.append(re.split('<|>', str(j))[-3])
        for j in i.findAll(class_='table-tournaments__bookmaker-coefficient'):
            flag2 += 1
            # print(j)
            if flag2 % 2 == 0:
                tri.append(str(re.split('<|>', str(j))[-3]))
                if len(tri) == 3:
                    main_coefficent.append(tri)
                    tri = []
        for j in i.findAll(class_='tab-content tab-content_active'):
            pass
            # print(j.findAll('b'))
    for m, j in enumerate(liga):
        ligaviy_dicktator[str(films).find(j)] = j
        # print(ligaviy_dicktator[str(films).find(j)])
    # print(ligaviy_dicktator)
    for i in team_one:
        tima_num = 0
        flyaga = 0
        tima_id = str(films).find(i)
        for j in list(ligaviy_dicktator.keys())[flyaga:]:
            # print(j, tima_id)
            flyaga += 1
            # print(j)
            if j < tima_id:
                tima_num = j
            else:
                if ligaviy_dicktator[tima_num] in ligaviy_dicktator_ligi.keys():
                    ligaviy_dicktator_ligi[ligaviy_dicktator[tima_num]].append(i)
                    break
                else:
                    ligaviy_dicktator_ligi[ligaviy_dicktator[tima_num]] = []
                    ligaviy_dicktator_ligi[ligaviy_dicktator[tima_num]].append(i)
                    break
    # print(ligaviy_dicktator_ligi)
    # print('Европа. Лига чемпионов УЕФА' in ligaviy_dicktator_ligi, ligaviy_dicktator_ligi)
    said = []
    for i in range(len(team_one)):
        # print(team_one[i])
        pobeda = str(sami_kontori_pri_pobede[i]).replace('"', '').replace("'", "")
        nichya = sami_kontori_pri_nichye[i].replace('"', '').replace("'", "")
        proigrish = sami_kontori_pri_proigrishe[i].replace('"', '').replace("'", "")
        if len(liga) > 1:
            for j in ligaviy_dicktator_ligi:
                if team_one[i] in ligaviy_dicktator_ligi[j]:
                    if not j in said:
                        print(j)
                        said.append(j)
        else:
            if not liga[0] in said:
                print(liga[0])
                said.append(liga[0])

        # print(pobeda == 'https://odds.ru/upload/media/default/0001/58/thumb_57363_default_big.svg')
        print(team_one[i] + " : " + team_two[i], main_coefficent[i])

        print(f'Лучшая контора для ставки на {team_one[i]}: {dicktator[pobeda]} ')
        print(f'Лучшая контора для ставки на ничью: {dicktator[nichya]}')
        print(f'Лучшая контора для ставки на {team_two[i]}: {dicktator[proigrish]}\n\n\n\n')



def basketball():
    odin = []
    dva = []
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    tri = []
    main_coefficent = []
    team_one = []
    team_two = []
    URL = "https://odds.ru/basketball/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='tab-contents')
    sami_kontori_pri_pobede = []
    sami_kontori_pri_nichye = []
    sami_kontori_pri_proigrishe = []
    flag = 0
    flag2 = 0
    flag_dlya_url = 0
    main_flag = 0
    liga = []
    ligaviy_flag = 0
    ligaviy_dicktator = {}
    ligaviy_dicktator_ligi = {}

    # for i in films:
    #     print(i.findAll(class_='table-tournaments__title table-tournaments__title_big'))
    for i in films:

        for j in i.findAll(class_='table-tournaments__title table-tournaments__title_big'):
            liga.append(str(str(j).split('>')[-2])[0:-3])
        for j in i.findAll(class_='table-tournaments__row table-tournaments__row_content table-tournaments__row_bk'):
            # print(j.findAll(class_='table-tournaments__bookmaker-name bookmaker-logo'))
            for z in j.findAll(class_='table-tournaments__bookmaker-name bookmaker-logo'):
                # print(i.find(class_='table-tournaments__title table-tournaments__title_big'))
                # print(z)
                if len(sami_kontori_pri_pobede) == len(sami_kontori_pri_nichye) == len(sami_kontori_pri_proigrishe):
                    sami_kontori_pri_pobede.append(
                        re.split('№;333#|"', str(z).replace('(', '№;333#').replace(')', '№;333#'))[-3])
                elif len(sami_kontori_pri_pobede) > len(sami_kontori_pri_nichye):
                    sami_kontori_pri_nichye.append(
                        re.split('№;333#|"', str(z).replace('(', '№;333#').replace(')', '№;333#'))[-3])
                else:
                    sami_kontori_pri_proigrishe.append(
                        re.split('№;333#|"', str(z).replace('(', '№;333#').replace(')', '№;333#'))[-3])
            for m, z in enumerate(j.findAll(class_='table-tournaments__team-name')):
                # print(int(str(i).find(re.split('"|<|>', str(z))[-3])), int(str(i).find(liga[ligaviy_flag])), len(liga))
                main_flag += 1
                if ligaviy_flag + 1 < len(liga):
                    #print(int(str(i).find(liga[ligaviy_flag])) < int(str(i).find(re.split('"|<|>', str(z))[-3])))
                    ligaviy_flag += 1
                # print(liga[ligaviy_flag])

                if main_flag % 2 == 1:
                    team_one.append(re.split('"|<|>', str(z))[-3])
                else:
                    team_two.append(re.split('"|<|>', str(z))[-3])
        for j in i.findAll(class_='table-tournaments__cell table-tournaments__cell_teams'):
            pass
            # print(j)
        # print(i)
        for j in i.findAll(class_='table-tournaments__bookmaker-mobile'):
            pass
        # print(j)
        for j in i.findAll('b'):
            # print(j)
            flag += 1
            if flag % 2 == 0:
                odin.append(re.split('<|>', str(j))[-3])
            else:
                dva.append(re.split('<|>', str(j))[-3])
        for j in i.findAll(class_='table-tournaments__bookmaker-coefficient'):
            flag2 += 1
            # print(j)
            if flag2 % 2 == 0:
                tri.append(str(re.split('<|>', str(j))[-3]))
                if len(tri) == 3:
                    main_coefficent.append(tri)
                    tri = []
        for j in i.findAll(class_='tab-content tab-content_active'):
            pass
            # print(j.findAll('b'))
    for m, j in enumerate(liga):
        ligaviy_dicktator[str(films).find(j)] = j
        # print(ligaviy_dicktator[str(films).find(j)])
    # print(ligaviy_dicktator)
    for i in team_one:
        tima_num = 0
        flyaga = 0
        tima_id = str(films).find(i)
        for j in list(ligaviy_dicktator.keys())[flyaga:]:
            # print(j, tima_id)
            flyaga += 1
            # print(j)
            if j < tima_id:
                tima_num = j
            else:
                if ligaviy_dicktator[tima_num] in ligaviy_dicktator_ligi.keys():
                    ligaviy_dicktator_ligi[ligaviy_dicktator[tima_num]].append(i)
                    break
                else:
                    ligaviy_dicktator_ligi[ligaviy_dicktator[tima_num]] = []
                    ligaviy_dicktator_ligi[ligaviy_dicktator[tima_num]].append(i)
                    break
    # print(ligaviy_dicktator_ligi)
    # print('Европа. Лига чемпионов УЕФА' in ligaviy_dicktator_ligi, ligaviy_dicktator_ligi)
    said = []
    for i in range(len(team_one)):
        # print(team_one[i])
        pobeda = str(sami_kontori_pri_pobede[i]).replace('"', '').replace("'", "")
        nichya = sami_kontori_pri_nichye[i].replace('"', '').replace("'", "")
        proigrish = sami_kontori_pri_proigrishe[i].replace('"', '').replace("'", "")
        if len(liga) > 1:
            for j in ligaviy_dicktator_ligi:
                if team_one[i] in ligaviy_dicktator_ligi[j]:
                    if not j in said:
                        print(j)
                        said.append(j)
        else:
            if not liga[0] in said:
                print(liga[0])
                said.append(liga[0])

        # print(pobeda == 'https://odds.ru/upload/media/default/0001/58/thumb_57363_default_big.svg')
        print(team_one[i] + " : " + team_two[i], main_coefficent[i])

        print(f'Лучшая контора для ставки на {team_one[i]}: {dicktator[pobeda]} ')
        print(f'Лучшая контора для ставки на ничью: {dicktator[nichya]}')
        print(f'Лучшая контора для ставки на {team_two[i]}: {dicktator[proigrish]}\n\n\n\n')



football()
# hockey()
# basketball()
