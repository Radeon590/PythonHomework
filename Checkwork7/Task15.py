def f(x, a1, a2):
    return ((5 <= x <= 30) == (14 <= x <= 23)) <= (a1 <= x <= a2)

results = []

for a1 in range(0, 101):
    for a2 in range(0, 101):
        for x in range(0, 100):
            if f(x, a1, a2) == 1:
                results.append((a2 - a1, a2))

print(max(results))