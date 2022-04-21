with open('26.txt') as f:
    money = int(f.readline().split(' ')[1])
    data = f.readlines()[0:]
    costs = []
    productTypes = []
    for i in range(0, len(data)):
        splited = data[i].split(' ')
        costs.append(int(splited[0]))
        productTypes.append(splited[1])
    costs = sorted(map(int, costs))
    results = []
    for i in range(0, len(costs)):
        if productTypes[i][0] == 'A':
            if costs[i] + sum(results) > money:
                break
            results.append(costs[i])
    print('max', max(results))
    for i in range(1, len(costs)):
        number = costs[len(costs) - i]
        if number <= max(results):
            break
        for j in range(0, len(results)):
            if sum(results) - results[j] + number <= money:
                results.remove(results[j])
                results.append(number)
    print('newMax', max(results))
    print('result', len(results), money - sum(results))