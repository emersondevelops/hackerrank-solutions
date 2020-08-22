T = int(input())
S = []

for i in range(T):
    S.append(input())

for i in S:
    for j in range(0, len(i), 2):
        print(i[j], end='')
    print(' ', end='')
    for j in range(1, len(i), 2):
        print(i[j], end='')
    print()
