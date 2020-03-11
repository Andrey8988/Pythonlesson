class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def pos(self):
        print(f"{self.name} {self.surname}, доход с премией : {sum(self._incom.values())}")
worker = Position("Vova", "Ivanov", "Arbeiter", 20000, 4000)
worker.pos()
