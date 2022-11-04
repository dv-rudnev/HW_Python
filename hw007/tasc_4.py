"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'Машина {self.name} остановилась.'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}.'

    def show_speed(self):
        return f'Машина {self.name} движется со скоростью: {self.speed}'

    def __str__(self):
        return f'Эта машина: {self.name}, цвет {self.color}, полицейская: {self.is_police}.'


class TownCar(Car):

    __speed_limit = 60

    def show_speed(self):
        if self.speed > self.__speed_limit:
            return f'Машина {self.name} движется со скоростью: {self.speed}.\n\
        Допустимая скорость ({self.__speed_limit}) для данного типа автомобиля превышена!'
        else:
            return f'Машина {self.name} движется со скоростью: {self.speed}.'


class SportCar(Car):

    pass


class WorkCar(Car):

    __speed_limit = 40

    def show_speed(self):
        if self.speed > self.__speed_limit:
            return f'Машина {self.name} движется со скоростью: {self.speed}.\n\
        Допустимая скорость ({self.__speed_limit}) для данного типа автомобиля превышена!'
        else:
            return f'Машина {self.name} движется со скоростью: {self.speed}.'


class PoliceCar(Car):

    pass


VAZ = TownCar(61, 'Баклажан', 'Девяточка', False)
BMW = SportCar(120, 'Black', 'BMW 520i', False)
GAZ = WorkCar(40, 'Зеленый', 'ГАЗ-66', False)
FORD = PoliceCar(130, 'Blue', 'Ford Crown Victoria', True)

print()
print(f'Машины в наличии: {VAZ.name}, {BMW.name}, {GAZ.name}, {FORD.name}.')
print(VAZ)
print(BMW)
print(GAZ)
print(FORD)
print(BMW.turn('налево'))
print(f'{BMW.is_police}.')
print(GAZ.turn('направо'), GAZ.stop())
print(VAZ.show_speed())
print(FORD.go())
# print(VAZ.__speed_limit)
