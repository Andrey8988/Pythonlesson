class OwnError(Exception):
    #def __init__(self, txt):
       # self.txt = txt

    def error(self, in_d):
        try:
            in_d = float(in_d)
        except ValueError:
            print("Это же буквы!" )
        else:
            z.append(in_d)
        finally:
            print("И снова:")

z = []
while True:
    if input("Чтобы ЗАКОНЧИТЬ нажмите q, \
\n  чтобы ПРОДОЛЖИТЬ нажмите ENTER  :") == 'q':
        print(z)
        break
    in_d = input("Введите число :  ")
    dd = OwnError(in_d)
    dd.error(in_d)