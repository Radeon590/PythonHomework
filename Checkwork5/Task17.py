def checkFn(a, b, c):
    a = a ** 2
    b = b ** 2
    c = c ** 2
    print(a, b, c)
    if a == b + c:
        return True
    elif b == a + c:
        return True
    elif c == a + b:
        return True
    else:
        return False

with open('17.txt') as f:
    data = f.readlines()
    counter = 0
    maximal = 0
    for i in range(2, 3):
        a = int(data[i])
        b = int(data[i - 1])
        c = int(data[i - 2])
        if checkFn(a, b, c):
            counter += 1
            maximal = max(maximal, (a + b + c))
    print('counter =', counter, 'max =', maximal)