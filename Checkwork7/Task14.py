n = 6 * 343 ** 1156 - 5 * 49 ** 1147 + 4 * 7 ** 1153 - 875
print(n)
def f(n, osn):
    result = []
    while n:
        result.append(str(n%osn))
        n //= osn
    return ''.join(result[::-1])
n = f(n, 7)
print(n)
print('result', sum([int(i) for i in n]))
