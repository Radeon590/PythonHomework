def f(a, b, c, d):
    return ((a and b) == (not(c))) and (b <= d)

print('a b c d')

for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if f(a, b, c, d):
                    print(a, b, c, d)