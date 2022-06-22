def f(number, border):
    if number == border:
        return 1
    if number < border:
        return 0
    return f(number - 1, border) + f(number // 2, border)

print(8 * f(13, 1))