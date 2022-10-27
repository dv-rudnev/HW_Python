# Модуль "интелекта" ботов

from random import randint

L = 1


def get_rusty(m: int):
    return randint(L, m)


def get_mashine(t: int, m: int):
    numb = t % (m + 1)
    return numb if numb != 0 else randint(L, m)