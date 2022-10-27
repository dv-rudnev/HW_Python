from print_tab import print_tab as ptb
from input_data import input_data
from check import check

print('''
    Крестики-нолики
Игровое поле выполнено в видедополнительной цифровой клавиатуры.
Вводимые цифры соответствуют полям. Притной игры.''')

def main(tab):
    counter = 0
    win = False
    while not win:
        ptb(tab)
        input_data("X", tab) if counter % 2 == 0 else input_data("O", tab)  # Смена игрока
        counter += 1
        if counter > 4:  # После 5го хода проверяем на победу.
            tmp = check(tab)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    print("Итоговая таблица:")
    ptb(tab)


tab = list(range(1,10))

if __name__ == '__main__':
    
    main(tab)