import requests
from bs4 import BeautifulSoup


def class_no_id(tag):
   return tag.has_attr('class') and not tag.has_attr('id')

# # КОММАНДЫ
# URL = "https://odds.ru/"
# request = requests.get(URL)
# soup = BeautifulSoup(request.text, "html.parser")
# films = soup.findAll('div', class_='table-tournaments__cell table-tournaments__cell_teams')
# for i in films:
#    film = i.find('b')
#    print(film)
#
# #КТО С КЕМ ИГРАЕТ
# URL = "https://odds.ru/"
# request = requests.get(URL)
# soup = BeautifulSoup(request.text, "html.parser")
# films = soup.findAll('div', class_='table-tournaments__cell table-tournaments__cell_teams')
# for i in films:
#    print(i.text)