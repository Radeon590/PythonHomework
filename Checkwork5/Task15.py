def f(A, x, y):
    return (x * y < 121) or (y > A) or (x >= A)

maximal = 0
for A in range(0, 100):
    flag = True
    for x in range(0, 100):
        if not(flag):
            break
        for y in range(0, 100):
            if not(f(A, x, y)):
                flag = False
                break
    if flag:
        maximal = max(maximal, A)
print(maximal)