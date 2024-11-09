from random import *
s = open(r'C:\Users\Учитель\Desktop\Города\Города.txt', encoding='utf-8').read().split()
z = 'йыьъ'

for x in range(len(s)):
    s[x] = s[x].lower()

first = choice(s)
s.remove(first)
last = first[-1]
if first[-1] in z:
    first = last[-2]
    if first[-2] in z:
        last = last[-3]

for q in range(10):
    print(f'Вам достался город на букву {last}')
    gorod = input()
    if gorod[0] == last:
        last = gorod[-1]
        if gorod[-1] in z:
            last = gorod[-2]
            if gorod[-2] in z:
                last = gorod[-3]
    else:
        continue
    for i in range(len(s)):
        if s[i][0] == last:
            a = i
            break
    gorod = s[a]
    print(gorod)
    if gorod[0] == last:
        last = gorod[-1]
        if gorod[-1] in z:
            last = gorod[-2]
            if gorod[-2] in z:
                last = gorod[-3]
    s.pop(a)
    






    
