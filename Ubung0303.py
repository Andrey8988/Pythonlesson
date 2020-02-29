def my_sum(arg_1, arg_2, arg_3):
    s = [arg_1, arg_2, arg_3]
    s.sort(reverse=True)
    x=s[0]+s[1]
    return x
erst=float(input("Введите число 1 "))
zwei=float(input("Введите число 2 "))
drei=float(input("Введите число 3 "))
print("Сумма двух наибольших аргументов = ", f"{my_sum(erst, zwei, drei):=.2f}")
