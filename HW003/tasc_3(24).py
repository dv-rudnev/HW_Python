# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import randint, uniform

size = randint(4, 6)
numb_float = []

# size = 5
# numb_float = [1.1, 1.2, 3.1, 5, 10.01]

for i in range(size):
    numb_float.append(round(uniform(1, 10), 2))
print(numb_float)

for i in range(size):
    numb_float[i] -= int(numb_float[i])
numb_float.sort()

dif = numb_float[-1] - numb_float[0]
print(round(dif, 2))
