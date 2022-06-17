with open('17.txt') as file:
    data = file.readlines()
    evenNumbersSum = 0
    evenNumbersCount = 0
    for i in range(0, len(data)):
        number = int(data[i])
        if number % 2 == 0:
            evenNumbersSum += number
            evenNumbersCount += 1
    evenNumbersAverage = evenNumbersSum // evenNumbersCount
    pairs = []
    for i in range(0, len(data) - 1):
        number1 = int(data[i])
        number2 = int(data[i + 1])
        if number1 % 3 == 0 or number2 % 3 == 0:
            if number1 < evenNumbersAverage or number2 < evenNumbersAverage:
                pairs.append(number1 + number2)
    print(len(pairs), max(pairs))
