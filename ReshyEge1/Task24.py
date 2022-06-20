with open('24.txt') as file:
    data = file.read()
    last4 = [' ', ' ', ' ', ' ']
    counter = 0
    maxCounter = 0
    for letter in data:
        last4.pop(0)
        last4.append(letter)
        if last4 == ['X', 'Z', 'Z', 'Y']:
            if counter > maxCounter:
                maxCounter = counter
            counter = 3
        else:
            counter += 1

    print(maxCounter)