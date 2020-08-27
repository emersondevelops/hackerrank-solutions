n = 7
c = [0, 0, 1, 0, 0, 1, 0]

jumps = 0
counter = 0
while counter < n:
    print(counter)

    if counter + 2 < n:
        if c[counter + 2] == 0:
            jumps += 1
            counter += 2
            continue
    if counter + 1 < n:
        if c[counter + 1] == 0:
            jumps += 1
            counter += 1
            continue
    counter += 1

print(jumps)
