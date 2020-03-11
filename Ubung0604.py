class Car:
    def __init__(self, speed, color, name, polis=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.polis = polis

    def stop(self):
        print(f"{self.name} stop")

    def start(self):
        print(f"{self.name} went")

    def turn(self):
        print(f"{self.name} turn")

    def show_speed(self):
        print(f"Speed of {self.name} {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
             print(f"{self.speed} km/uhr скорость превышена")
        else:
             print(self.speed)

class ArbaCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.speed} скорость превышена")
        else:
            print(self.speed)


class PolisCar(Car):
    def __init__(self, speed, color, name, polis=True):
        super().__init__(speed, color, name)

class SportCar(Car):
    print ("")

towncar = TownCar(70, "Blue", "Citywalker")
towncar.start()
towncar.stop()
towncar.turn()
towncar.show_speed()

sportcar = SportCar(70, "Rot", "Sprinter")
sportcar.start()
sportcar.stop()
sportcar.turn()
sportcar.show_speed()

workcar = ArbaCar(70, "Gelb", "Traktor")
workcar.start()
workcar.stop()
workcar.turn()
workcar.show_speed()

poliscar = PolisCar(70, "Blue", "SSS")
poliscar.start()
poliscar.stop()
poliscar.turn()
poliscar.show_speed()