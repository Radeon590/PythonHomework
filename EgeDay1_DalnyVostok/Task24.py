s = 'pqrsqqppppppp'
maxi = 0
cur = s[0]
print(cur[-1])
for i in range(1, len(s)):
    if cur[-1] + s[i] != 'qq':
        cur += s[i]
        maxi = max(maxi, len(cur))
    else:
        cur = s[i]

print(maxi)