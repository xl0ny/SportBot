# Импортируем необходимые классы.
import requests
from bs4 import BeautifulSoup
import re
import logging


# def football_live():
#     URL = "https://odds.ru/football/"
#     request = requests.get(URL)
#     soup = BeautifulSoup(request.text, "html.parser")
#     films = soup.findAll('div', class_='tab-contents')
#     times = []
#     flag = 0
#     for i in films:
#         for j in i.findAll(class_='table-tournaments__time'):
#             if j.findAll(class_='blinking'):
#                 times.append(re.split('"|<|>', str(j))[4])
#         for j in i.findAll(class_='table-tournaments__cell table-tournaments__cell_teams'):
#             if j.findAll(class_='table-tournaments__score color-green-primary'):
#                 print('счёт:', re.split('"|<|>', str(j.findAll(class_='table-tournaments__score color-green-primary')[0]))[-3] + '\n' + 'Время с начала матча:', times[flag], 'минут')
#                 print(re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[0]))[-3] + '  :  ' + re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[1]))[-3])
#                 print()
#                 print()
#                 flag += 1
#     if flag == 0:
#         print('нет активных матчей')


def football_live():
    URL = "https://odds.ru/football/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='tab-contents')
    schet_i_time = []
    teams = []
    times = []
    liga = []
    team_one = []
    ligaviy_dicktator = {}
    ligaviy_dicktator_ligi = {}

    flag = 0
    for i in films:
        for j in i.findAll(class_='table-tournaments__title table-tournaments__title_big'):
            liga.append(str(str(j).split('>')[-2])[0:-3])
        for j in i.findAll(class_='table-tournaments__time'):
            if j.findAll(class_='blinking'):
                times.append(re.split('"|<|>', str(j))[4])
            elif 'перерыв' in str(j):
                times.append('Перерыв')
        for j in i.findAll(class_='table-tournaments__cell table-tournaments__cell_teams'):
            if j.findAll(class_='table-tournaments__score color-green-primary'):
                team_one.append(re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[0]))[-3])
                if not times[flag] == 'Перерыв':
                    schet_i_time.append(' '.join(['счёт:', re.split('"|<|>', str(
                        j.findAll(class_='table-tournaments__score color-green-primary')[0]))[
                        -3] + '\n' + 'Время с начала матча:', times[flag], 'минут']))
                else:
                    schet_i_time.append(' '.join(['счёт:', re.split('"|<|>', str(
                        j.findAll(class_='table-tournaments__score color-green-primary')[0]))[
                        -3] + '\n' + 'В данный момент в игре перерыв']))
                teams.append(' '.join([re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[0]))[
                                           -3] + '  :  ' +
                                       re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[1]))[
                                           -3]]))
                flag += 1
        for m, j in enumerate(liga):
            ligaviy_dicktator[str(films).find(j)] = j
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
    said = []
    for i in range(flag):
        if len(liga) > 1:
            for j in ligaviy_dicktator_ligi:
                if team_one[i] in ligaviy_dicktator_ligi[j]:
                    if not j in said:
                        print(j)
                        said.append(j)
        print(schet_i_time[i])
        print(teams[i])
        print()
        print()
    if flag == 0:
        print('нет активных матчей')


def hockey_live():
    URL = "https://odds.ru/hockey/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='tab-contents')
    schet_i_time = []
    teams = []
    times = []
    liga = []
    team_one = []
    ligaviy_dicktator = {}
    ligaviy_dicktator_ligi = {}

    flag = 0
    for i in films:
        for j in i.findAll(class_='table-tournaments__title table-tournaments__title_big'):
            liga.append(str(str(j).split('>')[-2])[0:-3])
        for j in i.findAll(class_='table-tournaments__time'):
            if j.findAll(class_='blinking'):
                times.append(re.split('"|<|>', str(j))[4])
            elif 'перерыв' in str(j):
                times.append('Перерыв')
        for j in i.findAll(class_='table-tournaments__cell table-tournaments__cell_teams'):
            if j.findAll(class_='table-tournaments__score color-green-primary'):
                team_one.append(re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[0]))[-3])
                if not times[flag] == 'Перерыв':
                    schet_i_time.append(' '.join(['счёт:', re.split('"|<|>', str(
                        j.findAll(class_='table-tournaments__score color-green-primary')[0]))[
                        -3] + '\n' + 'Время с начала матча:', times[flag], 'минут']))
                else:
                    schet_i_time.append(' '.join(['счёт:', re.split('"|<|>', str(
                        j.findAll(class_='table-tournaments__score color-green-primary')[0]))[
                        -3] + '\n' + 'В данный момент в игре перерыв']))
                teams.append(' '.join([re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[0]))[
                                           -3] + '  :  ' +
                                       re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[1]))[
                                           -3]]))
                flag += 1
        for m, j in enumerate(liga):
            ligaviy_dicktator[str(films).find(j)] = j
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
    said = []
    for i in range(flag):
        if len(liga) > 1:
            for j in ligaviy_dicktator_ligi:
                if team_one[i] in ligaviy_dicktator_ligi[j]:
                    if not j in said:
                        print(j)
                        said.append(j)
        print(schet_i_time[i])
        print(teams[i])
        print()
        print()
    if flag == 0:
        print('нет активных матчей')


def basketball_live():
    URL = "https://odds.ru/basketball/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    films = soup.findAll('div', class_='tab-contents')
    schet_i_time = []
    teams = []
    times = []
    liga = []
    team_one = []
    ligaviy_dicktator = {}
    ligaviy_dicktator_ligi = {}

    flag = 0
    for i in films:
        for j in i.findAll(class_='table-tournaments__title table-tournaments__title_big'):
            liga.append(str(str(j).split('>')[-2])[0:-3])
        for j in i.findAll(class_='table-tournaments__time'):
            if j.findAll(class_='blinking'):
                times.append(re.split('"|<|>', str(j))[4])
            elif 'перерыв' in str(j):
                times.append('Перерыв')
        for j in i.findAll(class_='table-tournaments__cell table-tournaments__cell_teams'):
            if j.findAll(class_='table-tournaments__score color-green-primary'):
                team_one.append(re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[0]))[-3])
                if not times[flag] == 'Перерыв':
                    schet_i_time.append(' '.join(['счёт:', re.split('"|<|>', str(
                        j.findAll(class_='table-tournaments__score color-green-primary')[0]))[
                        -3] + '\n' + 'Время с начала матча:', times[flag], 'минут']))
                else:
                    schet_i_time.append(' '.join(['счёт:', re.split('"|<|>', str(
                        j.findAll(class_='table-tournaments__score color-green-primary')[0]))[
                        -3] + '\n' + 'В данный момент в игре перерыв']))

                teams.append(' '.join([re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[0]))[
                                           -3] + '  :  ' +
                                       re.split('"|<|>', str(j.findAll(class_='table-tournaments__team-name')[1]))[
                                           -3]]))
                flag += 1
        for m, j in enumerate(liga):
            ligaviy_dicktator[str(films).find(j)] = j
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
    said = []
    for i in range(flag):
        if len(liga) > 1:
            for j in ligaviy_dicktator_ligi:
                if team_one[i] in ligaviy_dicktator_ligi[j]:
                    if not j in said:
                        print(j)
                        said.append(j)
        print(schet_i_time[i])
        print(teams[i])
        print()
        print()
    if flag == 0:
        print('нет активных матчей')


# football_live()
# hockey_live()
# basketball_live()
