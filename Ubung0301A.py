# позиционные параметры
dm = int(input("Ведите делимое:"))
dst = int(input("Ведите делитель:"))
def first_func(dm, dst):
    """при делении на ноль - выводится ошибка"""
    return dm / dst
print("Результат выполнения функции:", first_func(dm, dst))


