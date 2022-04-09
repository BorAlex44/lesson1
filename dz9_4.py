class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула на {direction}'

    def show_speed(self):
        return f'Ваша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышаете водитель!!!!! Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.speed()} в норме'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышаете водитель!!!!! Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.speed} в норме'


class PoliceCar(Car):
    pass


town_car = TownCar(140, 'Желтая', 'Городская машина', False)
print(town_car.go())
print(town_car.show_speed())
sport_car = SportCar(240, 'Красная', 'Спортивная машина', False)
print(sport_car.turn('направо'))
work_car = WorkCar(30, 'Черная', 'Рабочая машина', False)
print(work_car.go())
print(work_car.show_speed())
police_car = PoliceCar(0, 'Синяя', 'Полицейская машина', True)
print(police_car.stop())
