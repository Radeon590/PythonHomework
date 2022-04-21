def f(s1, s2, turnNumber):
    if turnNumber == 1:#P
        return f(s1 + 1, s2, turnNumber + 1) and f(s1, s2 + 1, turnNumber + 1) and f(s1 * 2, s2, turnNumber + 1) and f(s1, s2 * 2, turnNumber + 1)
    if turnNumber == 2:#V
        if s1 + s2 >= 107:
            return False
        return f(s1 + 1, s2, turnNumber + 1) or f(s1, s2 + 1, turnNumber + 1) or f(s1 * 2, s2, turnNumber + 1) or f(s1, s2 * 2, turnNumber + 1)
    if turnNumber == 3:#P
        if s1 + s2 >= 107:
            return True
        return f(s1 + 1, s2, turnNumber + 1) and f(s1, s2 + 1, turnNumber + 1) and f(s1 * 2, s2, turnNumber + 1) and f(s1, s2 * 2, turnNumber + 1)
    if turnNumber == 4:#V
        if s1 + s2 >= 107:
            return False
        return f(s1 + 1, s2, turnNumber + 1) or f(s1, s2 + 1, turnNumber + 1) or f(s1 * 2, s2, turnNumber + 1) or f(s1, s2 * 2, turnNumber + 1)
    if turnNumber == 5 and s1 + s2 >= 107:
        return True


for i in range(1, 94):
    if f(13, i, 1):
        print(i)