from random import *

def proverka(gorod):
    zapret = 'йыьъ'
    if gorod[-1] in zapret:
        last = gorod[-2]
        print(f'Вам достался город на букву {last}')
        return last
    else:
        last = gorod[-1]
        print(f'Вам достался город на букву {last}')
        return last

def poisk(vybor):
    global s
    global q
    for b in range(len(s)):
        if s[b][0] == q:
            first_city = b
            break
    for c in range(len(s), 0, -1):
        if s[c][0] == q:
            last_city = с 
            break
    return s[randint(first_city, last_city)]

f = open(r"C:\Users\Учитель\Desktop\Города\Города.txt", encoding='utf-8').readlines()
s = [i.replace('\n', '').lower() for i in f]
for i in s:
    if i == '':
        s.remove(i)
gorod = choice(s)
print(gorod)
s.remove(gorod)
for i in range(10):
##    print(gorod)
    vybor = input()
    proverka(vybor)
    q = proverka(vybor)
    vybor_bota = poisk(q)
    print(vybor_bota)



