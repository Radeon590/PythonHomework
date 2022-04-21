def f(x, a1, a2):
    return (not(a1 <= x < a2) and (32 <= x <= 92)) <= (12 <= x <= 62)

result = []

for a1 in range(-1000, 1000):
    
    for a2 in range(-1000, 1000):
        flag = True
        for x in range(-1000, 1000):
            if not(f(x, a1, a2)):
                flag = False
                break
            if flag:
                result.append(a2 - a1)

print(len(result))
print(min(result))