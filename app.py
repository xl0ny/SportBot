import requests
from bs4 import BeautifulSoup
import re


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
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='table-tournaments__cell table-tournaments__cell_teams')
    for i in films:
        print(i.text.replace("\n", ""))

def main_component():
    URL = "https://odds.ru/football/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='main-component-tabs home-match-list')
    print(films)
    for i in films:
        film = i.find('b')
        print(film)

def new_get_maches():
    odin = []
    dva = []
    URL = "https://odds.ru/football/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='tab-contents')
    flag = 0
    for i in films:
        for j in i.findAll('b'):
            flag += 1
            if flag % 2 == 0:
                odin.append(re.split('<|>', str(j))[-3])
            else:
                dva.append(re.split('<|>', str(j))[-3])
    for i in range(len(odin)):
        print(dva[i] + " : " + odin[i])

new_get_maches()
# get_teams()