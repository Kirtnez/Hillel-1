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
        # elif user_n2 == 0: Почему так не будет работать елси он в блоке if ??
else:
    print(user_n1 / user_n2)