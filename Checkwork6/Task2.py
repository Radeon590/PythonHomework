print(oct(int('100010000110001', 2)))

def f(x, y, z, w):
    return ((x <= y) and (z or w)) <= ((x == w) or (y and not(z)))

print('x y z w')

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(f(x, y, z, w)):
                    print(x, y, z, w)