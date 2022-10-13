# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11



num = input('Введите число: ')

def SumDigits(n):
    n = str(n)
    sum = 0
    exsept = '0.,-'
    for i in n:
        if i not in exsept:
            sum += int(i)
    return sum


print(SumDigits(num))
