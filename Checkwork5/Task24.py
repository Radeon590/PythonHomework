with open('24.txt') as f:
    data = f.read().strip()
    seq = list(map(len, data.split('D')))
    maximal = 0
    for i in range(0, len(seq) - 1):
        if seq[i] + seq[i + 1] > maximal:
            maximal = seq[i] + seq[i + 1] + 1 #не уверен нужно ли делать + 1, просто ответ получался на 1 меньше нужного
    print(maximal)
