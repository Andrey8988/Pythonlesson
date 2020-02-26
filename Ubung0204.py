str01=input("Insert Zeile mit wort und Luecke  ").split()
for i, elem in enumerate(str01, start=0):
    s = str("".join(str01[i]))
    print(i+1, "-ое слово", s[:10])
