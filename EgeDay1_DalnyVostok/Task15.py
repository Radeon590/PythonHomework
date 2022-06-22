def f(A, x):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 90)

for A in range(1, 1000):
    if all(f(A, x) for x in range(1, 1000)):
        print(A)
        break