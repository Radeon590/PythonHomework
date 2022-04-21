result = []
for number in range(2422000, 2422081):
    flag = True
    for dev in range(2, round(number ** 0.5)):
        if number % dev == 0:
            flag = False
            break
    if flag:
        result.append(number)
for i in range(0, len(result)):
    print(i + 1, result[i])