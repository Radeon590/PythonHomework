with open('26.txt') as f:
    storage = int(f.readline().split(' ')[0])
    data = f.readlines()[0:]
    data = sorted(map(int, data))
    counter = 0
    sumOfNumbers = 0
    maximal = 0
    results = []
    for i in range(0, len(data)):
        number = data[i]
        if sumOfNumbers + number > storage:
            break
        sumOfNumbers += number
        counter += 1
        results.append(number)
        maximal = max(results)
    for i in range(0, len(data)):
        number = data[len(data) - 1 - i]
        for j in range(0, len(results)):
            if number <= maximal:
                break
            if sumOfNumbers - results[j] + number <= storage:
                maximal = number
    print('result:', counter, maximal)
    print(storage, sum(results))
