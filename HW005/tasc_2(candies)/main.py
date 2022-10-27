# Конфеты >o<

from random import randint
import engine as e


# Старт
print('''
-----------------------------------------------
           >o< >o<  Конфеты  >o< >o<
Все конфеты достаются сделавшему последний ход.
        Меньше 1 конфеты взять нельзя.
-----------------------------------------------''')


# Выберем тип игры и введем имена игроков
var_game = ['1', '2', '3', '99']
game_type = None
while game_type not in var_game:
    game_type = input('''
        1. Игрок против МАШИНЫ.
        2. Игрок против Игрока.
        3. Посмотреть на схватку МАШИНЫ и ЖЕЛЕЗЯКИ.
        Выберите тип игры (1, 2, 3): ''')
    # Введем имена игроков
    if game_type == '1':
        players_name = [input('\nВведите свое имя: '), 'МАШИНА']
    elif game_type == '2':
        players_name = [input('\nИмя первого игрока: '), input('Имя второго игрока: ')]
    elif game_type == '3':
        players_name = ['МАШИНА', 'ЖЕЛЕЗЯКА']
    elif game_type == '99':
        print('Сработал скрытый выход')
        exit()
    else:
        print('\nНекорректный ввод, повторите выбор.')

        
# Введем общее количество и количество конфет за ход
total = e.to_int(input('\nВведите общее количество конфет: '))
max_cpm = e.to_int(input('Сколько конфет можно забрать за ход: '))
print()

# Определим порядок хода
player = randint(0, 1)
print(f'    Первым ходит: {players_name[player]}')

# Играем
player, total = e.game(players_name, player, total, max_cpm)

# Финиш
e.winner(players_name[player], total)