for x in range(0, 1000):
    startX = x
    p = 1
    s = 0
    n = 0
    while x > 0:
        n += 1
        s += x % 3
        p *= x % 3
        x //= 3
    s += n
    p += n
    if s == 7 and p == 4:
        print(startX, s, p)