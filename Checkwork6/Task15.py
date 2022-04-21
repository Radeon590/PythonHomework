def belong(number, regionStart, regionEnd):
    return regionStart <= number and number <= regionEnd

def f(x, a1, a2):
    return (not(belong(x, a1, a2)) and (belong(x, 32, 92))) <= (belong(x, 12, 62))

minLength = 1000

for a1 in range(0, 100):
    for a2 in range(1, 100):
        isCorrect = True
        for x in range(0, 100):
            if not(f(x, a1, a2)):
                isCorrect = False
                break
        if isCorrect and a2 - a1 < minLength:
            minLength = a2 - a1

print(minLength)