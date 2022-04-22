def f(N):
    binN = bin(N)[2:]
    if N % 2 != 0:
        binN += '0'
    else:
        binN = '1' + binN
    if binN.count('1') % 2 == 0:
        binN += '1'
    else:
        binN += '0'
    return(binN)
for N in range(0, 100):
    if int(f(N), 2) > 228:
        print(N)
        break