for i in range(0, 1000):
    result = str(bin(i))[2:]
    if i % 2 == 0:
        result = '1' + result
    else:
        result = result + '0'
    if result.count('1') % 2 == 0:
        result += '1'
    else:
        result += '0'
    if int(result, 2) > 228:
        print(i)
        break