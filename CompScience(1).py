x = ['01', '101'] # расширить список до длины 5, соблюдая условие Фано
while len(x) < 5:
    x.append('0')
    for i in range(len(x)):
        if x[-1] == x[i][:1]:
            x[-1] == '1'