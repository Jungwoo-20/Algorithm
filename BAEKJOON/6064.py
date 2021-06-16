import sys

TC = int(sys.stdin.readline())

# x+M을 N으로 나누었을때 나머지가 y와 같아지게 되면 해결
for _ in range(TC):
    res = -1
    M, N, x, y = map(int, sys.stdin.readline().split())
    if x == M:
        x = 0
    if y == N:
        y = 0
    for i in range(x, M * N + 1, M):
        if i % N == y:
            res = i
            break

    print(res)
