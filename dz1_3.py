for i in range(1, 101):
    if i % 100 in (11, 12, 13, 14, 15) or i % 10 in (5, 6, 7, 8, 9, 0):
        print(i, ' процентов')
    elif i % 10 in (2, 3, 4):
        print(i, ' процента')
    else:
        print(i, ' процент')
