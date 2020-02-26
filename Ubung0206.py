anls={}
tov=[]
n=1
while True:
    if input("если хотите ввести новый товар  нажмите enter or n") == 'n':
        break
    tovls={}
    while True:
        if input("чтобы продолжить нажмите enter, чтобы закончить нажмите q") == 'q':
            break
        per=(input("введите характеристику по которой собираете данные о товаре, например название или цена или количество и проч "))
        print("введите ", per, "товара")
        rep=(input())
        tovls[per] = rep
        print(tovls)
    tov.append((n,tovls))
    print(tov)
    tovls=0
    n +=1







#n +=1
   # k=list(tovls.keys()
   # for f in tovls.keys():
   #     d=input(f'введите свойство товара  "{f}" ')
    #print(k)
#tovls[a] = '4'
   #     print(d)
