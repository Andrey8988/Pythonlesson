k =0
n=0
d = {}
with open("test07.txt", 'r', encoding="utf-8") as firm:
    for i in firm:  # выбор строки i
        imja, sobs, doch, isd, = i.split()
        doch = int(doch)
        isd = int(isd)
        s = doch - isd
        print(s, "Прибыль фирмы", imja)
        d[imja] = s
        if s > 0:
            k = k + s
            n += 1
    print("Сумма прибыли без учета убытков :", k)
su = k / n
print("Средняя прибыль без учета убыточных фирм :", su)
d['average'] = su
print("Словарь с фирмами и прибылями и средней", d)
import json
with open("test07a.json", 'w') as firm56:
    json.dump(d, firm56)





        #profi = {}
        #k = 0
       # s = (int(other[0]) - int(other[1])) #расчет прибыли
       #print(s)
        #if s > 0:
           # k = s + k
           # print(k)
