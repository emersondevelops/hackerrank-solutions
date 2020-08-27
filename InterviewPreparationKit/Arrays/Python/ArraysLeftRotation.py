n = 5
d = 4
a = [1, 2, 3, 4, 5]

for i in range(d % len(a)):

    a.append(a[0])
    a.pop(0)


print(a)
