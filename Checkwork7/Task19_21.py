def f(s1, s2, turn):
    if turn == 1:#П
        return f(s1 + 1, s2, turn + 1) and f(s1, s2 + 1, turn + 1) and f(s1 + s2, s2, turn + 1) and f(s1, s2 + s1, turn + 1)
    if turn == 2:#В
        if s1 + s2 >= 68: return False
        return f(s1 + 1, s2, turn + 1) or f(s1, s2 + 1, turn + 1) or f(s1 + s2, s2, turn + 1) or f(s1, s2 + s1, turn + 1)
    if turn == 3:#П
        #print(s1 + s2)
        if s1 + s2 >= 68: return True
        return f(s1 + 1, s2, turn + 1) and f(s1, s2 + 1, turn + 1) and f(s1 + s2, s2, turn + 1) and f(s1, s2 + s1, turn + 1)
    if turn == 4:#В
        if s1 + s2 >= 68: return False
        return f(s1 + 1, s2, turn + 1) or f(s1, s2 + 1, turn + 1) or f(s1 + s2, s2, turn + 1) or f(s1, s2 + s1, turn + 1)
    if turn == 5:#П
        if s1 + s2 >= 68: return True
        return False

for S in range(1, 60):
    if f(8, S, 1):
        print(S)