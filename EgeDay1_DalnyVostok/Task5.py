def f(N):
    binN = bin(N)[2:]
    if binN.count('1') % 2 == 0:
        binN = '10' + binN[2:] + '0'
    else:
        binN = '11' + binN[2:] + '1'
    return int(binN, 2)

for N in range(1, 100):
    if f(N) > 50:
        print(N)
        break