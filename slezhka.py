import requests
from bs4 import BeautifulSoup
import re
import logging


class Spain:
    @staticmethod
    def barcelona():
        URL = "https://www.sports.ru/barcelona/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def real_madrid():
        URL = "https://www.sports.ru/real/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def atletico():
        URL = "https://www.sports.ru/atletico/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def sevilia():
        URL = "https://www.sports.ru/sevilla/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def valencia():
        URL = "https://www.sports.ru/valencia/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def hetafe():
        URL = "https://www.sports.ru/getafe/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)

    @staticmethod
    def real_sociedad_san_sebastian():
        URL = "https://www.sports.ru/real-sociedad/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)

    @staticmethod
    def atletic_bilbao():
        URL = "https://www.sports.ru/athletic/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)

    @staticmethod
    def vilreal():
        URL = "https://www.sports.ru/villarreal/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def betis_sevilia():
        URL = "https://www.sports.ru/betis/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


class England:
    @staticmethod
    def liverpool():
        URL = "https://www.sports.ru/liverpool/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def manchester_city():
        URL = "https://www.sports.ru/manchester-city/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def manchester_united():
        URL = "https://www.sports.ru/mu/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def lester_city():
        URL = "https://www.sports.ru/leicester/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def chelsi():
        URL = "https://www.sports.ru/chelsea/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def wolverhampton_wanderers():
        URL = "https://www.sports.ru/wolves/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)

    @staticmethod
    def tottenham():
        URL = "https://www.sports.ru/tottenham/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)

    @staticmethod
    def arsenal():
        URL = "https://www.sports.ru/arsenal/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)

    @staticmethod
    def southampton():
        URL = "https://www.sports.ru/southampton/news/  "
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


    @staticmethod
    def newcastle():
        URL = "https://www.sports.ru/newcastle/news/"
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
        films = soup.findAll('div', class_='news')
        for i in films:
            for j in i.findAll('p'):
                # print(re.split('>|<', str(j.findAll('span')))[2])
                u = str(re.split('</a>|=', str(j.findAll('a')[0]))[-2]).replace('"', '').replace('<', '').replace('>', '').replace('strong', '').replace('/', '')
                print(u)


Spain.barcelona()