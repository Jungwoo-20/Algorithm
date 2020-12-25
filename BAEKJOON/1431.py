n = int(input())
serial = [input().rstrip() for _ in range(n)]


def sum(ser):
    cnt = 0
    for i in ser:
        if i.isdigit():
            cnt += int(i)
    return cnt


serial.sort(key=lambda x: (len(x), sum(x), x))
for i in serial:
    print(i)
