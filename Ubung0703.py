class Zelle:

    def __init__(self, zel):
        self.zel = zel

    def __str__(self):
        return self.zel

    def make_order(self, tra):
        return '\n'.join(['z' * tra for i in range(self.zel // tra)]) + '\n' + 'z' * (self.zel % tra)

    def __add__(self, other):
        return self.zel + other.zel

    def __sub__(self, other):
        return self.zel - other.zel if self.zel - other.zel > 0 \
        else "Schwach!"

    def __mul__(self, other):
        return self.zel * other.zel

    def __truediv__(self, other):
        return self.zel / other.zel

zelle_1 = Zelle(26)
zelle_2 = Zelle(24)
print(zelle_1 + zelle_2)
print(zelle_1 - zelle_2)
print(zelle_1 * zelle_2)
print(zelle_1 / zelle_2)
print(zelle_2.make_order(5))