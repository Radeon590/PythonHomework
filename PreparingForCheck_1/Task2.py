def f(w, x, y, z):
    return x and not(y and not(z or w))

print('w x y z')

for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if f(w, x, y, z): print(w, x, y, z)