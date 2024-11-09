##s = [4, 6, 7, 5, 6, 7, 1, 2, 8]
##print(s)
##for i in range(len(s)-1):
##    x1 = []
##    t = s[i]
##    x1.append(t) 
##    for j in range(i+1, len(s)-1):
##        x2 = []
##        q = s[j]
##        if t < q:
##            x2.append(x1[-1])
##        x2.append(q)
##        if s[j+1] > q:
##            x2.append(s[j+1])
##    if len(x2) > len(x1):
##        x2 = x1
##    
##print(x1)

#ракета       
##s = [1, 6, 3, 2, 5, 8]
##x = []
##for i in range(len(s)-1):
##    x1 = [s[i]]
##    for j in range(i+1, len(s)):
##        if s[j] > x1[-1]:
##            x1.append(s[j])
##    x.append(x1)
##xxx = []
##maxl = 0
##for q in x:
##    if len(q) > maxl:
##        maxl = len(q)
##for p in range(len(x)):
##    if len(x[p]) == maxl:
##        xxx.append(x[p])
##print(xxx)
##end = []
##for a in range(len(xxx)):
##    end += xxx[a]
##print(*set(end))
    

# Межпланетные перевозки
x = 1
y = 1
k = 2
##def (x, y, k):
##    s = x + y + k
##    if s % 2 == 0

s = x*y

s1 = (x+k)*y
s2 = x*(y+k)
s3 = (x+(k-i))*(y+(i))










