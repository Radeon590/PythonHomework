with open('27B.txt') as f:
    data = list(map(int, f.readlines()))
    counter = 0
    for i in range(1, len(data) - 1):
        for j in range(i + 1, len(data)):
            if (data[i] + data[j]) % 80 == 0:
                print('goodSum', data[i], data[j])
                if data[i] > 50 or data[j] > 50:
                    counter += 1
    print('result', counter)