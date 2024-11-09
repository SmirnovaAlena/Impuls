# перевод в любую с.с. из 10-й

##x = 12**12 + 24**5 - 18**3 + 1
##s = ''
##while x > 0:
##    s += str(x % 7)
##    x = x // 7
##print(s[::-1])

##s = str(bin(x)[2:])
##print(s.count('1'))


# Методы строк и их реализация
##s = '         Сегодня     прекрасный день        , а завтра        он будет ещё     прекраснее    (или нет)'
##while "  " in s:
##    s = s.replace("  ", " ")
##    s = s.replace(" ,", ",")
##if s[0] == " ":
##    s = s.replace(" ", "", 1)
##print(s)

# Заменить все чётные цифры в строке на 1
##s = input()
##chet = "02468"
##for i in s:
##    if i in chet:
##        s = s.replace(i, '1')
##print(s)

# Заменить все буквы a на A, кроме первого и последнего вхождения a
##s = 'qwertyaaaaaaaaaaqwerty'
##ind_first = s.find('a')
##ind_last = s.rfind('a')
##print(s[:ind_first + 1] + s[ind_first + 1:ind_last].replace('a','A') + s[ind_last:])




# Сделали кровью и потом
##s = '14abcYxbxczxbabcQsfahsabc5dfh'
##s = s.split('abc')
##first = s.pop(0)
##for i in range(len(s)):
##        if s[i][0].isdigit():
##                s[i] = s[i][1:]
##s = first + 'abc' + 'abc'.join(s)
##print(s)


# использование методов join() split()
##s = ['Киви', 'Банан', 'Ананас']
##s = ' + '.join(s)
##print(s)


# инструменты работы со списками
# сумма через цикл
##s = [1, 9, 6, 5, 3]
##summa = 0
##for i in range(len(s)):
##        summa += s[i]
##print(summa)

# сумма через внутрение функции
#найти кол-во различных элементов
##s = [1, 1, 9, 6, 9, 5, 5, 3, 3, 3]
##s2 = []
##for i in range(len(s)):
##        if s[i] not in s2:
##                s2.append(s[i])
##print(len(s2))
# найти кол-во различных элементов (через set)

##s = [1, 1, 9, 6, 9, 5, 5, 3, 3, 3]
##s = set(s)
##print(len(s))

# генератор списков из случайных чисел (random)
##from random import randint
##for i in range (10):
##        x = randint(1,10)
##        print(x)

# генератор списков
##from random import randint
##s = [_ for _ in range(10,30) if _ % 2 == 0]
##print(s)














