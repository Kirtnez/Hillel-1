import string

x = input("Введите текст #: ").title()
z = x.replace(" ", "")
for ch in string.punctuation:
    y = z.replace(, "")
print("#" + y)