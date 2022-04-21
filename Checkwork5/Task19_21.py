def f(s, turnNumber):
    if turnNumber == 1:#P
        return f(s + 1, turnNumber + 1) and f(s * 2, turnNumber + 1)
    if turnNumber == 2:#V
        if s >= 65:
            return False
        return f(s + 1, turnNumber + 1) or f(s * 2, turnNumber + 1)
    if turnNumber == 3:#P:
        if s >= 65:
            return True
        return f(s + 1, turnNumber + 1) and f(s * 2, turnNumber + 1)
    if turnNumber == 4:#V
        if s >= 65:
            return False
        return f(s + 1, turnNumber + 1) or f(s * 2, turnNumber + 1)
    return s >= 65

for i in range(1, 65):
    if f(i, 1):
        print(i)