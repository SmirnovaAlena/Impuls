##from itertools import product
##count = 0
##for i in product('01234567', repeat=5):
##    s = ''.join(i)
##    if s[0] != '0':
##        if s.count('6') == 1:
##            if all(pair not in s for pair in '16 61 36 63 56 65 76 67'.split()):
##                count += 1
##print(count)

##from itertools import permutations
##n = 'МАТВЕЙ'
##a = permutations(n)
##s = []
##for i in a:
##    s.append(list(i))
##count = 0
##for j in s:
##    flag = True
##    for i in range(len(j) - 1):
##        if j[0] == 'Й' or (j[i] == 'А' and j[i+1] == 'Е'):
##            flag = False
##    if flag == True:
##        count += 1
##print(count)


c = 0
for n in range(8**4, 8**5 + 1):
    x = oct(n)[2:]
    if x.count('1') == 0:
        for i in range(len(x) - 1):
            if int(x[i]) % 2 == int(x[i+1]) % 2 or x.count(x[i]) > 1:
                break
            if i == len(x) - 2:
                c += 1
print(c)
            










        





