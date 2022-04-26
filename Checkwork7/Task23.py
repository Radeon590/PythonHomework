def f(a):
    if a == 15:
        return 1
    if a > 15:
        return 0
    return f(a + 1) + f(a * 2) + f(a * 2 + 1) + f(a * 10)

print(f(1))