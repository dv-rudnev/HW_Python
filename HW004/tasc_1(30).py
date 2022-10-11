# 30. Вычислить число π c заданной точностью d
# Пример: при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

import math

pi = math.pi
from_user = str(input("Введите точность числа пи, например 0,001: "))

len_show = len(from_user) - 2
print(round(pi, len_show))