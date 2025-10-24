import string

x = input("Введите текст #: ").strip()
for ch in string.punctuation:
    x = x.replace(ch, "")
x = x.title()


x = x.replace(" ", "")
x = x[:140]
print("#" + x)
