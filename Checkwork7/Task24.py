with open("24-s1.txt") as f:
    data = f.readlines()
    max = (-1, 0)
    for lineNumber in range(0, len(data)):
        qNumber = data[lineNumber].count('Q')
        if qNumber >= max[1]:
            max = (lineNumber, qNumber)
    print(max)
    lineAlphabet = []
    for letter in data[max[0]]:
        if not(letter in lineAlphabet):
            lineAlphabet.append(letter)
    lineAlphabet.sort()
    lineAlphabet.remove('\n')
    print(lineAlphabet)
    minLetter = ('', 100)
    for letter in lineAlphabet:
        letterNumber = data[max[0]].count(letter)
        print(letter, letterNumber)
        if letterNumber > 0 and letterNumber < minLetter[1]:
            minLetter = (letter, letterNumber)
    print(minLetter)
    number = 0
    for line in data:
        number += line.count(minLetter[0])
    print('result', minLetter[0], number)