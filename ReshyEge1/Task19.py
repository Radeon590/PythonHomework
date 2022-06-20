def f(h1, h2, turn):
    if turn == 1:#Петя
        turn += 1
        return f(h1 + 1, h2, turn) and f(h1, h2 + 1, turn) and f(h1 * 2, h2, turn) and f(h1, h2 * 3, turn)
    if turn == 2:#Ваня
        turn += 1
        if h1 + h2 >= 69:
            return 0
        return f(h1 + 1, h2, turn) or f(h1, h2 + 1, turn) or f(h1 * 2, h2, turn) or f(h1, h2 * 3, turn)
    if turn == 3:#Петя
        turn += 1
        if h1 + h2 >= 69:
            return 1
        return f(h1 + 1, h2, turn) and f(h1, h2 + 1, turn) and f(h1 * 2, h2, turn) and f(h1, h2 * 3, turn)
    if turn == 4:#Ваня
        turn += 1
        if h1 + h2 >= 69:
            return 0
        return f(h1 + 1, h2, turn) or f(h1, h2 + 1, turn) or f(h1 * 2, h2, turn) or f(h1, h2 * 3, turn)
    if turn == 5:
        turn += 1
        if h1 + h2 >= 69:
            return 1
        return 0

for S in range(1, 59):
    if f(10, S, 1) == 1:
        print(S)