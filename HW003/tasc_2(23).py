# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

size = randint(4, 6)
numbers = []
multiplication = []

for i in range(size):
    numbers.append(randint(1, 10))
print(numbers)

if size % 2 != 0:
    n = int(size/2+1)
else:
    n = int(size/2)

for i in range(n):
    multiplication.append(numbers[i] * numbers[-i - 1])

print(f"Произведение пар чисел списка -> {multiplication}")
