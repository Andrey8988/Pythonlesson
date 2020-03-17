class Complex_numbers:
    def __init__(self, y, x):
        self.y = y
        self.x = x
    def __complex__(self, y, x):
        return complex(x + y)

c = Complex_numbers(50+2j, 2+1j)
print(c.__complex__(50+2j, 2+1j))
