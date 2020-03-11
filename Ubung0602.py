class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def on_road(self):
        r = 25
        k = 5
        s = self._length * self._width * r * k/1000  # обращаемся к атрибуту объекта
        print("Необходимо асфальта ", s, "тонн")

road = Road(20, 5000)
road.on_road()
