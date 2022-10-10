# 30. Вычислить число π c заданной точностью d
# Пример: при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

import math


from_user = str(input("Введите точность числа пи, например 0,001: "))
len_show = len(str(from_user).split('.,')[-1])
print(str(math.pi)[:len_show])
