##f = open(r"C:\Users\Учитель\Desktop\24_demo.txt").readline()
##s = [str(i) for i in f]
##maxs = 0
##current = 0
##for i in range(len(s)-1):
##    if s[i] != s[i+1]:
##        current += 1
##    else:
##        maxs = max(current, maxs)
##        current = 1
##print(maxs)


        
##f = open(r"C:\Users\Учитель\Desktop\24.txt").readline()
##s = [str(i) for i in f]
##v = [i for i in range(len(s)) if s[i] == 'V']
##mind = 10**6
##for i in range(len(v) - 119):
##    mind = min(v[i+119] - v[i], mind)
##print(mind+1)

##    if s[i] == 'X' and s[i+1] = 'Z' and s[i+2] == 'Z' and s[i+3] == 'Y':
f = open(r"C:\Users\Учитель\Desktop\24.txt").readline()
s = f.split('XZZY')
maxc = 0
n = []
for i in range(len(s)):
    n.append(len(s[i]))
print(max(n) + 6)
    
    














