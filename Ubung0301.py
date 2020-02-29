# позиционные параметры
k=1
print("Хотите поделить?")
while True:
    if input("Чтобы продолжить нажмите enter, чтобы закончить нажмите q ") == 'q':
        break
    dm = int(input("Ведите делимое:"))
    dst = int(input("Ведите делитель:"))
    if dst == 0:
        print("Пытаетесь делить на ноль? Начните-ка снова!")
    else:
        def first_func(dm, dst):
            return dm / dst
        print("Результат выполнения функции:", first_func(dm, dst))
k += 1



