# Передача оргтехники со склада в офис

class Firma:
    def __init__(self, place, place_number):
        self.place = place
        self.place_number = place_number

    def __str__(self):
        return f"\n PLACE: {self.place} PLACENUBER: {self.place_number}"


class Warehouse(Firma):
    def to_give(self, equip, *bureaus):
        for bureau in bureaus:
            bureau.to_take(equip)


class Bureau(Firma):
    def __init__(self, place, place_number):
        super().__init__(place, place_number)
        self.equipm = []

    def to_take(self, equip):
        self.equipm.append(equip)


class Equipment:
    def __init__(self, *equipment):
        self.equipment = list(equipment)

    def my_list(self):
        return self.equipment

eq = Equipment("printer", "skaner", "xerox")
wh = Warehouse("WareHouse", " N 3")
bra = Bureau("Bureau", "N 1")
brb = Bureau("Bureau", "N 2")
brc = Bureau("Bureau", "N 3")
wh.to_give(eq, bra, brb, brc)

print(wh)
print(f"{bra}; {brb}; {brc}")
print(bra.equipm[0].my_list())
