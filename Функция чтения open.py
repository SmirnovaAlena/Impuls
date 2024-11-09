##file = open(r"C:\Users\Учитель\Desktop\17.txt").readlines()
##s = [int(i) for i in file]
##maxsum = -20001
##c = 0
##for i in range(len(s) -1):
##    if s[i] % 3 == 0 or s[i+1] % 3 == 0:
##        c += 1
##        maxsum = max(maxsum, s[i] + s[i+1])
##print(c, maxsum)

##file = open(r"C:\Users\Учитель\Desktop\17(сложный).txt").readlines()
##s = [int(i) for i in file]
##c = 0
##maxsum = 0
##sumeven = 0
##ceven = 0
##for i in s:
##    if i % 2 == 0:
##        sumeven += i
##        ceven += 1
##sr_arifm = sumeven / ceven
##print(sr_arifm)
##for i in range(len(s) -1):
##    if (s[i] % 3 == 0 or s[i+1] % 3 == 0) and (s[i] < sr_arifm or s[i+1] < sr_arifm):
##        c += 1
##        maxsum = max(maxsum, s[i] + s[i+1])
##print(c, maxsum)

import time
import os
start = time.time()
file = open(r"C:\Users\Учитель\Desktop\17 (1).txt").readlines()
s = [int(i) for i in file]
c = 0
minsum = 3000000
max_15 = -1000000
for i in s:
    if i % 100 == 15:
        max_15 = max(max_15, i)
for i in range(len(s) - 2):
    if (999 < s[i] < 10000 and (s[i+1]  > 9999 or s[i+1] < 1000) and (s[i+2]  > 9999 or s[i+2] < 1000)) or \
    (999 < s[i+1] < 10000 and (s[i]  > 9999 or s[i] < 1000) and (s[i+2]  > 9999 or s[i+2] < 1000)) or \
    (999 < s[i+2] < 10000 and (s[i]  > 9999 or s[i] < 1000) and (s[i+1]  > 9999 or s[i+1] < 1000)):
        if s[i] + s[i+1] + s[i+2] < max_15:
            c += 1
            minsum = min(minsum, s[i] + s[i+1] + s[i+2])
print(c, minsum)
end = time.time()
print(end-start)

        






        








