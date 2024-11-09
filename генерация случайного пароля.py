# генерация случайного пароля
from random import *
numbers = [str(_) for _ in range(10)]
letters = list('qwertyuiopasdfghjklzxcvbnm')
big_letters = list('QWERTYUIOPASDFGHJKLZXCVBNM')
signs = list('!+-=#№$')
common_list = numbers + letters + big_letters + signs
easy, hard = 0, 0
for _ in range(100):
    password = ''
    d = randint(6, 15)
    for i in range(d):
        password += choice(common_list)
    count_num, count_let, count_signs = 0, 0, 0
    for q in password:
        if q in numbers:
            count_num += 1
        elif q in letters or q in big_letters:
            count_let += 1
        elif q in signs:
            count_signs += 1
    if (count_signs == 0) and (len(password) < 10) and (count_let == len(password)):
        print(password, 'this is an easy password')
        easy += 1
    if (count_signs >= 1) and (len(password) >= 12) and (count_let > 0) and (count_num > 0) and (password[0] in numbers):
        print(password, 'this is an HARD password')
        hard += 1
print('Количество простых паролей =', easy/100)
print('Количество сложных паролей=', hard/100)






