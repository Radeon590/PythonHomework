n = 6 * 3431156 - 5 * 491147 + 4 * 71153 - 875

def f(n, osn):
    result = []
    while n > osn:
        result.append(n % osn)
        n = n // osn
    result.append(n)
    return(result)
    strResult = ''
    for i in result:
        strResult = str(i) + strResult
    return(strResult)

n = f(n, 7)
print(n)
print('result', sum(n))
