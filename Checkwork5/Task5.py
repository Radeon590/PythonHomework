def f(n, counter):
    print('log', n)
    if n / 2 == 19 or n - 1 == 19:
        print('result', counter + 1)
        return
    if not(n % 2 == 0):
        n -= 1
        counter += 1
    else:
        n = n // 2
        counter += 1
    f(n, counter)


f(629, 0)

print('')
nn = 19
for i in range(0, 10):
    nn = nn * 2
    print(nn)