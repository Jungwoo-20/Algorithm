import sys

n = int(sys.stdin.readline())
for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    line = m - n
    current = 0
    cnt = 0
    move_cnt = 1
    while current < line:
        cnt += 1
        current += move_cnt
        if cnt % 2 == 0:
            move_cnt += 1

    print(cnt)
