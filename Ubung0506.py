slov ={}
with open("test06.txt", 'r') as sho:
    for i in sho: #выбор строки i
        uhr = 0
        imja, *other = i.split()
        for k in other: #k - выбор элемента в строке
            if k != "-": #проверка соответствия
                uhr += int(k[:k.find("(")]) #отделяем цифру и складываем с другими
                slov[imja] = uhr
    print(slov)
