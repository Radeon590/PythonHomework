for i in range(2422000, 2422081):
    easyNumber = True
    for b in range(2, round(i ** 0.5)):
        if i % b == 0:
            easyNumber = False
            break
    if easyNumber:
        print(i)