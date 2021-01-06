import sys

N = int(sys.stdin.readline())

while N > 0:
    n, m = map(int, sys.stdin.readline().split())

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())

    print(n - 1)
    N-=1