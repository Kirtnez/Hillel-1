print ("Hello, user")

n1 = int(input("Введите число: "))
n2 = 0

while n1 > 0:
    Num = n1 % 10
    n1 = n1 // 10

    n2 = n2 * 10
    n2 = n2 + Num


print('"Обратное" ему число:', n2)
