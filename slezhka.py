import requests
from bs4 import BeautifulSoup
import re
import logging

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
"Арсенал": "arsenal",
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
"Зенит Санкт-Петербург": "zenit",
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
"Крылья Советов Самара": "krylia-sovetov"}

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


russia = {"Зенит Санкт-Петербург": "zenit",
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

def get_news(team):
    URL = f"https://www.sports.ru/{team}/news/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='news')
    masiv = []
    for i in films:
        for j in i.findAll('p'):
            # print(re.split('>|<', str(j.findAll('span')))[2])
            u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>',
                                                                                                              '').replace(
                'strong', '').replace('/', '')
            masiv.append(u)
    masiv = masiv
    return masiv


# get_news(france["Брест"])
# get_news(england["Ливерпуль"])
