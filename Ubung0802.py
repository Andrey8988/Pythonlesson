class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
in_d = input("Enter divisor ")
try:
    in_d = float(in_d)
    k = 100 / in_d
except ValueError:
    print("Das ist wort!" )
except ZeroDivisionError:
    print("Das ist nicht gut - divis 0")
else:
    print(f"OK - {k}")
finally:
    print("fin")