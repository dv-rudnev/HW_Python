# ДЗ№3(24). Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = [1.1, 1.2, 3.1, 5, 10.01]

print(lst)
'''Старое решение'''
# lst = [round(val % 1, 2) for val in lst]

'''Новое решение'''
lst = list(map(lambda val: round(val % 1, 2), lst))

print(max(lst) - min(lst))
