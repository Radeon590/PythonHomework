def transfer(number, base):
    counter = 0
    result = ''
    while number >= base:
        ost = str(number % base)
        if ost == '0':
            counter += 1
        result += ost
        number //= base
    return counter

n = 6 * 512 ** 95 + 7 * 64 ** 96 + 3 * 8 ** 98 + 5 * 8 ** 93 + 100

print(transfer(n, 64))