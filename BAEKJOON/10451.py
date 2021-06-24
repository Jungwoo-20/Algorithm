import sys

T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    N = int(sys.stdin.readline())
    lst = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        tmp = i
        while visited[tmp] == 0 and i != visited[tmp]:
            visited[tmp] = i
            tmp = lst[tmp]
        if i == visited[tmp]:
            cnt += 1
    print(cnt)
