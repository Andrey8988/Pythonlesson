class Stationery:
    def __init__(self, title):
        self.title = title
    def drow(self):
        print(f"Запуск отрисовки")
class Pen(Stationery):
    def drow(self):
        print(f"Drow with {self.title} gut")
class Pencil(Stationery):
    def drow(self):
        print(f"Drow with {self.title} slecht")
class Handle(Stationery):
    def drow(self):
        print(f"Drow with {self.title} tui-tui")
stati = Stationery("All")
stati.drow()
stati = Pen("Pen")
stati.drow()
stati = Pencil("Pencil")
stati.drow()
stati = Handle("Handle")
stati.drow()