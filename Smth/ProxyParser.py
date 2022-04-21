with open('http.txt') as f:
    data = f.readlines()
    for i in range(0, len(data)):
        data[i] = 'http://' + data[i]
