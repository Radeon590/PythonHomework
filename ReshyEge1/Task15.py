def f(x, y, A):
    return (2 * x + 3 * y < 30) or (x + y >= A)

for A in range(0, 100):
    good = True
    for x in range(0, 100):
        for y in range(0, 100):
            if f(x, y, A) != 1:
                good = False
                break
        if good == False:
            break
    if good == True:
        print(A)


