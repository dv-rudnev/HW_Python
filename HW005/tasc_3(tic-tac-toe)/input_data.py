def input_data(token, tab):
    valid = False
    while not valid:
        answer = input("Куда поставим " + token + "? ")
        try:
            answer = int(answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if answer >= 1 and answer <= 9:
            if (str(tab[answer-1]) not in "XO"):
                tab[answer-1] = token
                valid = True
            else:
                print ("Это поле уже занято.")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9.")