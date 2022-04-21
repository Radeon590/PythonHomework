with open("24.txt") as f:
    s = f.readline()
    count = 1
    maximum = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1] == 'X':
            count += 1
            maximum = max(count, maximum)
        else:
            count = 1
    print(maximum)