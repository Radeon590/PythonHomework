maxS = 0
for s in range(0, 10000):
    n = 1
    while s > 200:
        s = s - 15
        n = n + 3
    if n == 46 and s > maxS:
        print(s)
        maxS = s
print('result', maxS)

