data = '1' * 45 + '2' * 45
while '111' in data:
    data = data.replace('111', '2', 1)
    data = data.replace('222', '1', 1)

print(data)
print(9 ** 3)