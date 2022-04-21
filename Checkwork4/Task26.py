with open('26.txt') as f:
    data = f.readlines()
    data = sorted(data)
    balance = 982000
    sum = 0
    sumA = 0
    for i in range(0, len(data)):
        number = int(data[i].split()[0])
        if sum + number > balance:
            sum -= int(data[i - 1].split()[0])
            maxJNumber = -5
            for j in range(i + 1, len(data)):
                jNumber = int(data[j].split()[0])
                jLetter = data[j].split()[1]
                if jNumber <= balance - sum and jNumber > maxJNumber:
                    maxJNumber = jNumber
            if maxJNumber == -5:
                print('none')
                sum += int(data[i - 1].split()[0])
            else:
                sum += maxJNumber
                if jLetter == 'A' and not(data[i - 1].split()[1] == 'A'):
                    sumA += 1
            print(sumA, balance - sum)
            break
        sum += number
        if data[i].split()[1] == 'A':
            sumA += 1
