def print_line():
    print(' ---+---+---')


def print_tab(tab):
    print()
    for i in range(2, -1, -1):
        print(' ', tab[0+i*3], '|', tab[1+i*3], '|', tab[2+i*3], ' ')
        if i != 0: print_line()
    print()
