with open('24.txt') as f:
    data = f.read()
    counter = 0
    results = []
    for i in range(0, len(data)):
        if data[i] == 'X':
            counter += 1
        else:
            results.append(counter)
            counter = 0
    print(max(results))