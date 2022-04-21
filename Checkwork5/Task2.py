print(bin(4)[2:])
print(oct(10010001101)[2:])

def f(x, y, z, w):
    return ((x or not(y)) and (not(z) == w)) <= (y and z)

print('x y z w')

for x in range (0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
             for w in range(0, 2):
                 if f(x, y, z, w) == 0:
                     print(x, y, z, w)

#answer: yzwx