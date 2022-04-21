elementsSum = 0

def F(n):
    if n > 2:
        print(n)
        F(n - 3)
        F(n - 4)
        return elementsSum
F(10)
print(10 + 7 + 4 + 3 + 6 + 3)