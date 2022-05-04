import requests
from bs4 import BeautifulSoup
import re
import logging
import time

all_teams = {"Барселона": "barcelona",
             "Реал мадрид": "real",
             "Атлетико мадрид": "atletico",
             "Севилья": "sevilla",
             "Валенсия": "valencia",
             "Хетафе": "getafe",
             "Реал Сосьедад": "real-sociedad",
             "Атлетик Бельбао": "athletic",
             "Вильярреал": "villarreal",
             "Реал Бетис": "betis",
             "Ливерпуль": "liverpool",
             "Манчестер сити": "manchester-city",
             "Манчестер Юнайтед": "mu",
             "Лестер сити": "leicester",
             "Челси": "chelsea",
             "Вулверхэмптон": "wolves",
             "Тоттенхэм Хотспур": "tottenham",
             "Арсенал": "arsenal",
             "Саутгемптон": "southampton",
             "Ньюкасл Юнайтед": "newcastle",
             'Фламенго Рио-де-Жанейро': 'flamengo',
             'Палмейрас Сан-Паулу': 'palmeiras',
             "Гремио Порту-Алегри": "gremio",
             "Атлетико Паранаэнсе Куритиба": "atletico-paranaense",
             "Сантос": "santos",
             "Сан-Паулу": "sao-paulo",
             "Интернасьонал Порту-Алегри": "internacional",
             "Крузейро Белу-Оризонти": "cruzeiro",
             "Атлетико Минейро Белу-Оризонти": "atletico-mineiro",
             "Куритиба": "curitiba",
             "Пари Сен-Жермен ПСЖ Париж": "psg",
             "Лион": "lyon",
             "Марсель": "marseille",
             "Ренн": "rennes-fc",
             "Лилль": "lille",
             "Монпелье": "montpellier",
             "Реймс": "reims",
             "Страсбур": "strasbourg",
             "Ницца": "nice",
             "Брест": "stade-brestois-29",
             "Аякс Амстердам": "ajax-fc",
             "АЗ Алкмаар": "az",
             "ПСВ Эйндховен": "psv",
             "Фейеноорд Роттердам": "feyenoord",
             "Виллем Тилбург": "willem-ii",
             "Витесс Арнем": "vitesse",
             "Гронинген": "groningen",
             "Херенвен": "heerenveen",
             "Хераклес Алмело": "heracles",
             "Ювентус": "juventus",
             "Интер Милан": "inter",
             "Аталанта": "atalanta",
             "Лацио": "lazio",
             "Рома": "roma",
             "Наполи Неаполь": "napoli",
             "Кальяри": "cagliari",
             "Парма": "parma",
             "Милан ": "milan",
             "Торино Турин": "torino",
             "Бенфика Лиссабон": "benfica",
             "Порту": "porto",
             "Спортинг": "sporting",
             "Брага": "braga",
             "Витория Гимараеш": "vitoria-guimaraes",
             "Боавишта": "boavista",
             "Риу Аве Вила-ду-Конди": "rio-ave-fc",
             "Жил Висенте Барселуш": "gil-vicente",
             "Фамаликан": "famalicao",
             "Морейренсе": "moreirense",
             "Зенит": "zenit",
             "Краснодар": "krasnodar",
             "ЦСКА Москва": "cska",
             "Ростов": "rostov",
             "Арсенал Тула": "arsenal-tula ",
             "Локомотив": "lokomotiv",
             "Спартак": "spartak",
             "Уфа": "ufa",
             "Тамбов": "fc-tambov",
             "Динамо": "dynamo",
             "Оренбург": "orenburg",
             "Урал": "ural",
             "Ахмат": "akhmat",
             "Сочи": "fc-sochi",
             "Рубин Казань": "rubin",
             "Крылья Советов Самара": "krylia-sovetov",
             "Базель": "fc-basel",
             "Янг Бойз Берн": "young-boys",
             "Цюрих": "zurich",
             }

spain = {"Барселона": "barcelona",
         "Реал мадрид": "real",
         "Атлетико мадрид": "atletico",
         "Севилья": "sevilla",
         "Валенсия": "valencia",
         "Хетафе": "getafe",
         "Реал Сосьедад": "real-sociedad",
         "Атлетик Бельбао": "athletic",
         "Вильярреал": "villarreal",
         "Реал Бетис": "betis"
         }

england = {"Ливерпуль": "liverpool",
           "Манчестер сити": "manchester-city",
           "Манчестер Юнайтед": "mu",
           "Лестер сити": "leicester",
           "Челси": "chelsea",
           "Вулверхэмптон": "wolves",
           "Тоттенхэм Хотспур": "tottenham",
           "Арсенал": "arsenal",
           "Саутгемптон": "southampton",
           "Ньюкасл Юнайтед": "newcastle"
           }

braziliya = {'Фламенго Рио-де-Жанейро': 'flamengo',
             'Палмейрас Сан-Паулу': 'palmeiras',
             "Гремио Порту-Алегри": "gremio",
             "Атлетико Паранаэнсе Куритиба": "atletico-paranaense",
             "Сантос": "santos",
             "Сан-Паулу": "sao-paulo",
             "Интернасьонал Порту-Алегри": "internacional",
             "Крузейро Белу-Оризонти": "cruzeiro",
             "Атлетико Минейро Белу-Оризонти": "atletico-mineiro",
             "Куритиба": "curitiba"
             }

france = {"Пари Сен-Жермен ПСЖ Париж": "psg",
          "Лион": "lyon",
          "Марсель": "marseille",
          "Ренн": "rennes-fc",
          "Лилль": "lille",
          "Монпелье": "montpellier",
          "Реймс": "reims",
          "Страсбур": "strasbourg",
          "Ницца": "nice",
          "Брест": "stade-brestois-29"
          }

gollandia = {"Аякс Амстердам": "ajax-fc",
             "АЗ Алкмаар": "az",
             "ПСВ Эйндховен": "psv",
             "Фейеноорд Роттердам": "feyenoord",
             "Виллем Тилбург": "willem-ii",
             "Витесс Арнем": "vitesse",
             "Гронинген": "groningen",
             "Арсенал": "arsenal",
             "Херенвен": "heerenveen",
             "Хераклес Алмело": "heracles"
             }

italia = {"Ювентус": "juventus",
          "Интер Милан": "inter",
          "Аталанта": "atalanta",
          "Лацио": "lazio",
          "Рома": "roma",
          "Наполи Неаполь": "napoli",
          "Кальяри": "cagliari",
          "Парма": "parma",
          "Милан ": "milan",
          "Торино Турин": "torino"
          }

portugalia = {"Бенфика Лиссабон": "benfica",
              "Порту": "porto",
              "Спортинг": "sporting",
              "Брага": "braga",
              "Витория Гимараеш": "vitoria-guimaraes",
              "Боавишта": "boavista",
              "Риу Аве Вила-ду-Конди": "rio-ave-fc",
              "Жил Висенте Барселуш": "gil-vicente",
              "Фамаликан": "famalicao",
              "Морейренсе": "moreirense"
              }

switzerland = {"Базель": "fc-basel",
               "Янг Бойз Берн": "young-boys",
               "Цюрих": "zurich",
               }

russia = {"Зенит": "zenit",
          "Краснодар": "krasnodar",
          "ЦСКА Москва": "cska",
          "Ростов": "rostov",
          "Арсенал Тула": "arsenal-tula ",
          "Локомотив": "lokomotiv",
          "Спартак": "spartak",
          "Уфа": "ufa",
          "Тамбов": "fc-tambov",
          "Динамо": "dynamo",
          "Оренбург": "orenburg",
          "Урал": "ural",
          "Ахмат": "akhmat",
          "Сочи": "fc-sochi",
          "Рубин Казань": "rubin",
          "Крылья Советов Самара": "krylia-sovetov"
          }
broken_needle = ['пари сёна-жермен псж парижа', 'хетафы', 'реал сосьедад', 'палмейрас сан-паулы', 'гремио порта-алегри',
                 'интернасьонал порта-алегри', 'крузейро бела-оризонти', 'атлетико минейро бела-оризонти', 'ренн',
                 'фейеноорд роттердов', 'витесс арнема', 'херенвен', 'хераклес алмётшего', 'аталанта', 'кальяри',
                 'порта', 'жил висенте барселуш', 'морейренса', 'арсенал тула']


def get_news(team):
    URL = f"https://www.sports.ru/{team}/news/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='news')
    masiv = []
    was = []
    for i in films:
        for j in i.findAll('p'):
            # print(str(j).find('data-news-dtime'))
            data_vihoda = str(re.split('data-news-dtime="|" data-news-id|:', str(j))[1]).replace('"', '').replace('<',
                                                                                                                  '').replace(
                '>',
                '').replace(
                'strong', '').replace('/', '')[:10]
            # print(data_vihoda)
            # print(re.split('>|<', str(j.findAll('span')))[2])
            u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>',
                                                                                                              '').replace(
                'strong', '').replace('/', '')
            masiv.append(
                u + '\n\n' + 'Дата выхода новости: ' + data_vihoda + '  ' + re.split('>|<', str(j.findAll('span')))[
                    2] + 'МСК')
            # print(re.split('>|<', str(j.findAll('span')))[2])
    masiv = masiv
    return masiv


def get_news_since_to(team='psg', since='55 12 2 5 2023'):
    noww = time.strftime("%M %H %d %m %Y", time.localtime())
    nowww = []
    team_news = ''
    now = ' '
    result = []
    # print(noww)
    for i in noww.split():
        if not i[0] == '0':
            nowww.append(i)
        else:
            nowww.append(i[1:])
    now = now.join([i for i in nowww])
    now = time.strptime(str(now), "%M %H %d %m %Y")
    # print(now)
    team_times_news = {}
    since = time.strptime(since, "%M %H %d %m %Y")
    for i in get_news(team):
        for j in i.split('\n'):
            # print(team_news)
            if j[:11] == 'Дата выхода':
                pass
                team_time = []
                for u in ' '.join(
                        [i for i in re.split('-| |:', (j.split()[-2] + " " + j.split()[-1])[:-3])[::-1]]).split():
                    if not u[0] == '0':
                        team_time.append(u)
                    else:
                        team_time.append(u[1:])
                team_time = time.strptime(" ".join([i for i in team_time]), "%M %H %d %m %Y")
                team_times_news[team_time] = team_news
            else:
                if j:
                    team_news = j
                # print(team_news)
    for i in team_times_news.keys():
        if since < i < now:
            result.append(team_times_news[i])
        else:
            break
    return result

# get_news_since_to('psg', "36 14 2 5 2022")
# for i in get_news('psg'):
#     print(i)
# print(get_news('psg'))
# get_news(france["Брест"])
# get_news(england["Ливерпуль"])
