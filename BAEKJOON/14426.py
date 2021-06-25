import sys

N, M = map(int, sys.stdin.readline().split())
lst = [sys.stdin.readline().rstrip() for _ in range(N)]
cnt = 0
for _ in range(M):
    tmp = sys.stdin.readline().rstrip()
    for i in lst:
        if i.startswith(tmp):
            cnt += 1
            break
print(cnt)
