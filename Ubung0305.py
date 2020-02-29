k = 0
end=0
while True:
    if input("ЕСЛИ ХОТИТЕ ВВОДИТЬ ПОСЛЕДОВАТЕЛЬНОСТЬ, нажмите enter, если хотите ВЫЙТИ - q :") == 'q':
        break
    str01 = input("Введите последовательность чисел через пробел, ЕСЛИ ВВЕДЕТЕ w ПОЛУЧИТЕ ИТОГ :").split()
    if str01[len(str01) -1] == 'w':
        if str01[len(str01) -1] == 'w':
            end=1
        str01=str01[:-1]
  #  print(str01)
    for i, elem in enumerate(str01, start=0):
        s = float("".join(str01[i]))
        k = k + s
    print("Summa =", k)
    if end == 1:
        break



