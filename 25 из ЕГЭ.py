# 25 из ЕГЭ

##for x in range(201455, 201471):
##    cdel = 0
##    sd = []
##    for d in range(1, x+1):
##        if x % d == 0:
##            cdel += 1
##            sd.append(d)
##    if cdel == 4:
##        print(sd)

##c = 0
##for x in range(500000, 510000):
##    if c == 5:
##        exit
##    else:
##        for d in range(18, x//2 + 1, 10):
##            if x % d == 0:
##                print(x, d)
##                c += 1
##                break

##for a in range(0, 9):
##    for b in range(0, 999):
##        s = '3' + str(a) + '1' + str(b) + '57'
##        if int(s) % 2023 == 0:
##            print(int(s))

##from fnmatch import *
##for x in range(0, 10**8, 2023):
##    if fnmatch(str(x), '3?1*57'):
##        print(x, x//2023)

c = 0
for x in range(452022, 453000):
    sd = []
    for d in range(2, x//2 + 1):
        if x % d == 0:
            sd.append(d)
    if len(sd) > 1:
        m = sd[0] + sd[-1]
        if m % 7 == 3:
            c += 1
            print(x, m)
    if c == 5:
        break








        


