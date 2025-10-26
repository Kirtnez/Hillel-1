import string
s = input("Значение:")
q, d = s.split('-')

letters = string.ascii_letters
print(letters[letters.index(q) : letters.index(d) + 1])
