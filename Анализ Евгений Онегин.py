f = open(r"C:\Users\Учитель\Desktop\Частотный анализ текста\yevgeniy-onegin.txt", encoding='utf-8').read()
s = [str(i).lower() for i in f]
letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
analys = [0]*33
k = 0
for i in letters:
    c = s.count(i)
    analys[k] = c
##    print(analys[k])
    k += 1

m = set(s)
print(len(m))
    

    

