import itertools

s = '0123456789'

for k in range(3):
    for x in itertools.product(s, repeat=k):
        unmaskedPart = ''.join(x)
        result = int('1234' + unmaskedPart + '58')
        if result % 19 == 0:
            print(result, result / 19)
