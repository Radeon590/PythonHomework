for x in range(10000, 100000):
    a, b = 0, 1
    startX = x
    while x > 0:
        a = a + 1
        b = b * (x % 1000)
        x = x // 1000
    print(a, b, startX)
    if a == 2 and b == 11:
        print('result', startX)
        break
