maximal = 2
result = 84131
for number in range(84052, 84131):
    counter = 2
    for dev in range(2, round(number ** 0.5)):
        if number % dev == 0:
            counter += 1
    print('number', number, 'counter', counter)
    if counter > maximal:
        maximal = counter
        result = number
    elif counter == maximal:
        result = min(result, number)
counter = 0
for dev in range(1, result + 1):
    if result % dev == 0:
        counter += 1
print(counter, result)
