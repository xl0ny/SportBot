import requests
from bs4 import BeautifulSoup
import re
import logging

spain = {"Барселона": "barcelona",
    "Реал мадрид":"real",
    "Атлетико мадрид":"atletico",
    "Севилья":"sevilla",
    "Валенсия":"valencia",
    "Хетафе":"getafe",
    "Реал Сосьедад":"real-sociedad",
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


def get_news(team):
        URL = f"https://www.sports.ru/{team}/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)

# get_news(spain["Барселона"])
# get_news(england["Ливерпуль"])