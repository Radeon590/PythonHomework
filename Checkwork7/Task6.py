result = []
for d in range(0, 1000):
    startD = d
    n = 1
    while d // n > 0:
        d = d - 2
        n = n + 3
    if n == 46:
        result.append(startD)
print(max(result) + min(result))
print(18 * 8)