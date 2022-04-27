result = []
for i in range(87921, 88188):
    strI = str(i)
    sum = 0
    multiplied = 1
    for number in strI:
        numberInt = int(number)
        sum += numberInt
        multiplied = multiplied * numberInt
    if sum % 14 == 0 and multiplied % 18 and multiplied != 0:
        result.append((sum, multiplied))
result.sort()
print(result)