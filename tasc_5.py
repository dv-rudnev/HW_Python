# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math  

x1, y1 = int(input("Введите X точки А: ")), int(input("Введите Y токи А: "))
x2, y2 = int(input("Введите X точки B: ")), int(input("Введите Y токи B: "))

# sqrt = ((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)) ** 0.5
print(f"Длинна отрезка {round(float(math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))), 3)}")