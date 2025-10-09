user_n1 = float (input("Введите первое число: "))
user =  input("Знак (+-/*) :")
user_n2 = float (input("Введите второе число число: "))

if user == "+":
    print(user_n1 + user_n2)

elif user == "-":
    print(user_n1 - user_n2)

elif user == "/":
    print(user_n1 / user_n2)

elif user == "*":
    print(user_n1 * user_n2)

        #Хотел добавить ещё условий для красоты, но понял то значит "Работает - не трогай"