with open('27B.txt') as f:
    data = f.readlines()
    counter = 0
    for i in range(1, len(data) - 1):
        for j in range(i + 1 , len(data)):
            if int(data[i]) * int(data[j]) % 26 == 0:
                counter += 1
    print(counter)