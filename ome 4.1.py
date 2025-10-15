w = [0, 1, 0, 12, 3 ]
a = []
s = []
for num in w:
    if num == 0:
        s.append(num)
    else:
        a.append(num)
x = a + s
print(x)