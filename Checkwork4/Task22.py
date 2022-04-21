for i in range(0, 1000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a += x % 8
        if x % 2 == 0:
            b *= x % 8
        x = x // 8
    if a == 14 and b == 24:
        print(i)
        break