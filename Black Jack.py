from random import *
import time
cbot, cplayer = 0, 0
n = int(input('До какого кол-ва побед продолжаем игру?\n'))
while cbot < n and cplayer < n:
    koloda = [2, 3, 4]*8 + [5, 6, 7, 8, 9, 10, 11]*4
    shuffle(koloda)
    score_pl, score_bot = 0, 0
    flag = True                       # флаг для начала игры бота
    cards = []
    while True:
        if score_pl > 21:
            print('У Вас перебор, победу одержал бот')
            cbot += 1
            flag = False
            break
        elif score_pl == 21:
            print('У Вас Black Jack! Вы выиграли')
            flag = False
            cplayer += 1
            break
        else:
            print('Хотите вязть карту?')
            igrok = input('Нажмите y, если хотите ещё. Нажмите n, если достаточно')
            if igrok == 'y':
                card = koloda.pop()
                cards.append(card)
                score_pl += int(card)
                print(f'Вам выпала карта {card}\nСписок Ваших карт {cards}')
            elif igrok == 'n':
                break
    while flag:
        bot_cards = ''
        while score_bot <= randint(17, 19):
            if score_bot < 21:
                bot_card = koloda.pop()
                score_bot += bot_card
                time.sleep(1)
                bot_cards += (str(bot_card) + ' ')
                print(f'Боту выпала карта {bot_card}\nСписок карт бота {bot_cards}')
            if score_bot > 21:
                print('У бота перебор')
                flag = False
                cplayer += 1
                break
            if score_bot == 21:
                print('У бота Black Jack. Бот выиграл')
                flag = False
                cbot += 1
                break
    if score_pl < 21 and score_bot < 21:
        if score_pl > score_bot:
            print(f'Вы победили!\nУ Вас {score_pl} очков\nУ бота {score_bot} очков')
            cplayer += 1
        if score_pl < score_bot:
            print(f'Вы проиграли! Бот победил\nУ Вас {score_pl} очков\nУ бота {score_bot} очков')
            cbot += 1
        if  score_pl == score_bot:
            print(f'Ничья...\nУ Вас {score_pl} очков\nУ бота {score_bot} очков')
    print(f'Текущий счёт {cplayer} : {cbot}')


