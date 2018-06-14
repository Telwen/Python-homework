# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car():
    def __init__(self,speed, color, name, _is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = _is_police

    def go (self):
        print('Машина начала движение')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'налево':
            print('Машина повернула налево')
        if direction == 'направо':
            print('Машина поверну', direction)

class TownCar(Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    pass

