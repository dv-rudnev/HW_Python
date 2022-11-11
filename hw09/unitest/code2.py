"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    '''Дорога...'''
    _lenght = 0
    _width = 0

    def __init__(self, lenght, width, dens, thickness):
        self._lenght = lenght  # в метрах
        self._width = width  # в метрах
        self.dens = dens  # в кг на кв.м/см
        self.thickness = thickness  # в метрах

    def calc_asphalt_mass(self):
        '''Расчет массы асфальта'''
        weight_in_kg = int(self._lenght * self._width * self.dens * self.thickness)
        weight_in_tons = int(weight_in_kg / 1000)
        return (f'{self._lenght}м*{self._width}м*{self.dens}кг*{self.thickness}м = {weight_in_kg} кг = {weight_in_tons} т')


road_e95 = Road(5000, 20, 25, 0.05)

if __name__ == '__main__':
    print(road_e95.calc_asphalt_mass())
    # print(type(road_e95.calc_asphalt_mass()))
    