def f(N):
    binN = bin(N)[2:]
    while len(binN) < 8:
        binN = '0' + binN
    print(binN)
    binN = binN.replace('1', '-')
    binN = binN.replace('0', '1')
    binN = binN.replace('-', '0')
    print(binN)

f(120)
print(int('10000111', 2))
print(int('10001000', 2))