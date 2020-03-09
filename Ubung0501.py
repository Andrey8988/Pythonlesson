while True:
    k = input("Word  :").split()
    if not k:
        break
    with open("test02.txt", "a") as grund:
        for i in range(len(k)):
            grund.write(k[i] + '\n')
            #print(grund.closed)
grund = open("test02.txt", 'r')
c = grund.read()
print(c)
grund.close()
