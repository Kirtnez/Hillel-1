while True:
    user_n1 = float (input("Введите первое число: "))
    user =  input("Знак (+-/*) :")
    user_n2 = float (input("Введите второе число число: "))
    if user == "+":
        print(user_n1 + user_n2)

    elif user == "-":
        print(user_n1 - user_n2)

    elif user == "*":
        print(user_n1 * user_n2)

    elif user == "/":
        if user_n1 == 0:
            print ("Ошибка")

        else:
            print(user_n1 / user_n2)
    else:
        print("Ошибка")

    x = (input("Хотите продолжить? (y/n): "))
    if x == "n":
        print("Конец")
        break
    elif x == "y" :
        continue
    else:
        print("Неверный ввод.")
    break
