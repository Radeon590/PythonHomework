result = []

def F(n):
    if n > 2:
        result.append(n)
        print(n)
        F(n - 3)
        F(n - 4)

F(10)
print('sum', sum(result))