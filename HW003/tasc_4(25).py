# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal_int = int(input('Введите десятичное число для преобразования в двоичное: '))
binary_str = ''

while decimal_int > 0:
    binary_str = str(decimal_int % 2) + binary_str
    decimal_int = decimal_int // 2

print(decimal_int, '->', binary_str)