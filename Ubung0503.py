with open("test03.txt") as rock:
    x = []
    y = []
    z = rock.read().split("\n") #разбивка на подстроки по переводу строки
    #print(z)
    for i in z:
        i = i.split() #разбивка подстрокИ на подострОки по пробелу
        if int(i[1]) < 20000: # первод второго элемента в формат и сравнение
            x.append(i[0])
        y.append(i[1])
        print()
print("Сотрудники с низкими ЗП", x)
print("Средняя зарплата - ", sum(map(int, y)) / len(y))

