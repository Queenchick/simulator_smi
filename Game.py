# alfa version 0.1

import random
import time
import os

media_name_tabu = ['Meduza', 'Медуза', 'Радио Свобода', 'Radio Liberty', 'The Insider', 'Инсайдер', 'Ukr',
                   'Put pid',
                   'Путин пид', 'pid', 'пид', 'Пут лох', 'loh', 'лох']
event = {1: 'сборная России по футболу проиграла Ниггерии', 2: 'Утонул корабль "Панорама"',
         3: 'США объявила войну Сирии', 4: 'Россия начала специальную военную операцию на Украине'}

preZident_tabu = ['Путяша', 'Кадыров', 'Шарлатан', 'Россия', 'тоталитарн', 'Вторжение в', 'Украин', 'новичок',
                  'свобода', 'навальн']

respect_for_vatniks = 0
max_respect_of_persons = 100
respect_of_persons = 0
max_respect_for_vatniks = 100
respectthe_russian_authorities = 0
maxrespectthe_russian_authorities = 100
warnings = 0
max_warnings = 3





def media():
    global a
    print(
        f'Добро пожаловать в симулятор своб****** (Данное слово запрещенно Роскомнадзором с 2023 года(Статья 13.21)) '
        f'сми в россии')
    time.sleep(1)
    os.system('cls')
    name = input('Как будет называться ваше сми агенство?\n')
    if name in media_name_tabu:
        print('Ваше агенство запретили на территории РФ по 3 статье ЗАКОНА РФ "О СРЕДСТВАХ МАССОВОЙ ИНФОРМАЦИИ"')
        a = ''
        while a != 'Y':
            a = input('Начать все заново? Y/n\n')
            media()
    else:
        print('Удачи! и запомни: не слова про политику')


def media_genre():
    print('Про что вы будете писать статьи?')
    genre = 'полит'
    while 'полит' in genre:
        genre = input("Про ")
        if 'политику' in genre or 'полит' in genre:
            print('Последнее предупреждение!')
    print('отлично! С завтрашнего дня вы начнете свою работу')


def article_writing():
    global event, respect_for_vatniks, max_respect_of_persons, respect_of_persons, max_respect_for_vatniks, \
        respectthe_russian_authorities, maxrespectthe_russian_authorities, warnings, max_warnings
    c = []
    for i in event.keys():
        c.append(i)
    while warnings != max_warnings:
        a = random.choice(c)
        print(*event[a], end='!')
        print()
        article_ = input('Будете писать статью? Y/n\n')
        if a == 3 and article_ == 'Y' or a == 4 and article_ == 'Y':
            print(*'Минюст РФ подозревает в вас')
            print()
            warnings += 1
            respect_of_persons += 10
        else:
            respectthe_russian_authorities += 10
        if respectthe_russian_authorities == maxrespectthe_russian_authorities:
            respect_of_persons -= respect_of_persons
            respect_for_vatniks = max_respect_for_vatniks
            print('Теперь вы "государственное" сми')


if __name__ == '__main__':
    media()
    time.sleep(2)
    media_genre()
    time.sleep(2)
    article_writing()
