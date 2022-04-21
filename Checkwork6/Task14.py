def translateFunc(number, numberingSystem):
    devidingResult = number
    result = []
    while number >= numberingSystem:
        result.append(number % numberingSystem)
        number = number // numberingSystem
    result.append(number)
    resultString = ''
    for i in result:
        resultString = str(i) + resultString
    return resultString

number = 729 ** 6 + 3 ** 14 - 36
translatedNumber = translateFunc(number, 9)
print(translatedNumber.count('0'))
