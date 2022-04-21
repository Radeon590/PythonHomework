def f(fileName):
    counter = 0
    with open(fileName) as f:
        data = f.readlines()
        for i in range(1, len(data)):
            print(i)
            for j in range(1, len(data)):
                if not(i == j):
                    n1 = int(data[i])
                    n2 = int(data[j])
                    if n1 > 50 or n2 > 50:
                        if (n1 + n2) % 80 == 0:
                            counter += 1
    return(counter)

a = f('27A.txt')
b = f('27B.txt')
print('answer', a, b)