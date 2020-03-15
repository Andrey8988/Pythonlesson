from abc import ABC, abstractmethod

class Kleid(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def konsum(self):
        pass

class Mantel(Kleid):
    @property
    def konsum(self):
        return self.size/6.5 + 0.5

class Anzug(Kleid):
    @property
    def konsum(self):
        return self.size*2 + 0.3

mn = Mantel(120)
anz = Anzug(120)
print("Расход на костюм", round(anz.konsum, 2))
print("Расход на пальто", round(mn.konsum, 2))
print("Bсего ткани необходимо :", round(mn.konsum + anz.konsum, 2))
