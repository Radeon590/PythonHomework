with open('17.txt') as f:
    data = f.readlines()
    counter = 0
    maxSum = 0
    for i in range(1, len(data)):
        number1 = int(data[i])
        number2 = int(data[i -1])
        if number1 % 3 == 0 or number2 % 3 == 0:
            counter += 1
            if number1 + number2 > maxSum:
                maxSum = number1 + number2
    print(counter, maxSum)