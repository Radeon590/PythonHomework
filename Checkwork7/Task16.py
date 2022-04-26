import sys

sys.setrecursionlimit(5000)

def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 3 + f(n / 2 - 1)
    if n > 1 and n % 2 != 0:
        return n + f(n + 2)

for n in range(900, 1000):
    print('f(n)', f(n))