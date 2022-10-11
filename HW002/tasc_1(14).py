# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11


from dataclasses import replace

str_numb = (input('Введите вещественное число: '))
str_numb_tmp = str_numb.split()
print(str_numb_tmp)
# summa = sum(str_numb_tmp[::])
# print(str_numb, '->', summa)