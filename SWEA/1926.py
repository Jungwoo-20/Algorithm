for c in [str(x) for x in range(1, int(input()) + 1)]:
    count = c.count('3') + c.count('6') + c.count('9')
    if count:
        print('-' * count, end =" ")
    else:
        print(c, end =" ")