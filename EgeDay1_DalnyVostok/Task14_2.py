def transfer(number, base):
    result = ''
    counter = 0
    while number >= base:
        ost = str(number % base)
        if not(ost in result):
            counter += 1
        result += ost
        number //= base
    return counter

n = 216 ** 6 + 216 ** 4 + 36 ** 6 - 6 ** 14 - 24

print(transfer(n, 6))