for x in range(0, 1000):
    startX = x
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if (x % 2) != 0:
            M = M + x % 8
        x = x // 8
    if L == 3 and M == 6:
        print(startX)