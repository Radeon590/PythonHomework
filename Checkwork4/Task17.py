with open('17.txt') as f:
    numbers = [int(x) for x in f]
    counter = 0
    sum = 0
    for i in range(1, len(numbers)):
        if numbers[i] % 3 == 0 or numbers[i - 1] % 3 == 0:
            counter += 1
            if numbers[i] + numbers[i - 1] > sum:
                sum = numbers[i] + numbers[i - 1]
print(counter, sum)
