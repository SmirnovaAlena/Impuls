# игра кости (для шести кубиков)
from random import *
result = [0]*11
smart_bot, lucky_bot, draw = 0, 0, 0

for i in range (10**6):
    bet_smart = 21
    bet_lucky = randint(6, 36)
    q1 = randint(1,6)
    q2 = randint(1,6)
    q3 = randint(1,6)
    q4 = randint(1,6)
    q5 = randint(1,6)
    q6 =randint(1,6)
    s = q1 + q2 + q3 + q4 + q5 + q6
    
    if abs(bet_smart - s) < abs(bet_lucky - s):
        smart_bot += 1
    if abs(bet_smart - s) > abs(bet_lucky - s):
        lucky_bot += 1
    if abs(bet_smart - s) == abs(bet_lucky - s):
        draw += 1

print(smart_bot/10**6, lucky_bot/10**6, draw/10**6)
