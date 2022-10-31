# ДЗ№2(16)ю Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input("Введите число N: "))

x = 0
'''Старое решение'''
for i in range(1, n + 1):
    b = (1 + (1 / i)) ** i
    x += b
print(f"Для n = {n}, сумма = {round(x, 2)}")

'''Новое решение'''
tmp = [(1 + (1 / i)) ** i for i in range(1, n + 1)]
x = round(sum(list(map(lambda a: + a, tmp))), 2)
# x = round(sum(list(map(lambda a: + a, [(1 + (1 / i)) ** i for i in range(1, n + 1)]))), 2)
print(x)