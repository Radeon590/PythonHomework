def f(w, x, y, z):
    return not(x <= w) or (y <= z) or not(y)

print('w x y z')

for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if f(w, x, y, z) == 0:
                    print(w, x, y, z)