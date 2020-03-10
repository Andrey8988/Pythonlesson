with open("test05.txt", 'w') as dana:
    dana.write("5 4 7 4 ")
with open("test05.txt", 'r') as dana:
    dana2 = dana.read().split()
    # print(dana2)
    # print(type(dana2))
    # print(type(dana2[0]))
    def sma(x):
        """функция перевода данных в список и сумма списка"""
        y = []
        for i in x:
            y.append(int(i))
        return sum(y)
print("Summa :", sma(dana2))
