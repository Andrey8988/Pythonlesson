n=0
with open("test01.txt") as gru:
    for z in gru:
        n += 1
        k =z.split()
        print("Строка :", z, "В строке слов", len(k))
    print("Кол-во строк", n)




