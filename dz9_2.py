class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        massa = self._lenght * self._width * self.weight * self.height / 1000
        return massa


new_road = Road(5000, 20)
print(f'Для покрытия всего дорожного полотна неободимо {new_road.asphalt_mass()} тонн')
