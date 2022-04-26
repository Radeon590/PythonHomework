results = []

for x in range(0, 10000):
    startX = x
    L, M = 0, 0
    while x > 12:
        L = L + 1
        x = x // 4
        M = x
    if L > M:
        L, M = M, L
    if L == 3 and M == 7:
        results.append(startX)

print(max(results))