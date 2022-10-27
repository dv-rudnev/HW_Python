from time import sleep
import ii
from sys import exit


def to_int(val: str):
    if val:
        return int(val)
    else:
        print('Вы все сломали...')
        exit()
        

def viev(name: str, move: int):
    print(f'{name}, сколько конфет берем?')
    print(move)
    sleep(1)


def winner(name: str, total: int):
    print(f'\nОставшиеся конфеты: {total}, разом забирает игрок: {name}.')
    print(f'>o< >o<  Победитель {name}  >o< >o<\n')


def game(p_name: list, player: int, ttl: int, max_cpm: int):
    while ttl > max_cpm:
        print(f'\n    Конфет осталось: {ttl}')

        # Ход
        move = 0
        if p_name[player] == 'МАШИНА':
            move = ii.get_mashine(ttl, max_cpm)
            viev(p_name[player], move)

        elif p_name[player] == 'ЖЕЛЕЗЯКА':
            move = ii.get_rusty(max_cpm)
            viev(p_name[player], move)

        else:
            while True:
                move = to_int(input(f'{p_name[player]}, сколько конфет берем?\n'))
                if 0 < move <= max_cpm:
                    break
                elif move == 99:
                    print('Сработал скрытый выход.')
                    exit()
                else:
                    print(f'\n!   Что-то не так, введите число в диапазоне 1 - {max_cpm}.\n    Конфет осталось: {ttl}\n')


        # Меняем игрока
        player = 0 if player else 1

        ttl -= move
    return (player, ttl)