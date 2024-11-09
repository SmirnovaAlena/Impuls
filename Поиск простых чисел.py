# алгоритм поиска больших (>10**6) простых чисел
##import time
##p = 99000991
##d = 0
##start = time.time()
##for i in range(2, round(p**0.5)):
##    if p % i == 0:
##        d += 1
##print(d)
##end = time.time()
##print(end-start)

##import time
##
##w = 0
##start = time.time()
##for p in range(1_000_000, 2_000_000):
##    c = 0
##    for i in range(2, round(p**0.5)):
##        if p % i  == 0:
##            c += 1
##    if c == 0:
##        w += 1
##print(w)
##end = time.time()
##print(end-start)
            
# задача о диапазоне чисел
##         
##x = 11**4
##sp_del = []
##for d in range(2, x//2 + 1):   # поиск делителей на отрезке от 2 до x//2 + 1
##    if x % d == 0:
##        sp_del.append(d)
##print(x, sp_del)

# поиск совершенных чисел в диапазоне от 1 до 10000
##for x in range(2, 10001):
##    sd = []
##    for d in range(1, x//2 + 1):
##        if x % d == 0:
##            sd.append(d)
##    if x == sum(sd):
##        print(x, sd)
            














