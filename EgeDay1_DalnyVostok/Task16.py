def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n - 2) - f(n - 1)
    if n > 2 and n % 2 != 0:
        return 2 * f(n - 1) - f(n - 2)

print(f(27))