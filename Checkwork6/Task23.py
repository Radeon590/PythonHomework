def f(a):
    if a == 30:
        return 1
    if a > 30:
        return 0
    return f(a + 1) + f(a + 2) + f(a + 4)

print(f(21))