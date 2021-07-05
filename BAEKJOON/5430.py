import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    lst = sys.stdin.readline().rstrip()[1:-1].split(',')
    f, b, r = 0, 0, 0
    p = p.replace('RR', '')
    if len(lst) < p.count('D'):
        print('error')
        continue
    for j in p:
        if j == 'R':
            r += 1
        elif j == 'D':
            if r % 2 == 0:
                f += 1
            else:
                b += 1
    if f + b <= n:
        lst = lst[f:n - b]
        if r % 2 == 0:
            print('[' + ','.join(lst) + ']')
        else:
            print('[' + ','.join(lst[::-1]) + ']')
    else:
        print('error')
