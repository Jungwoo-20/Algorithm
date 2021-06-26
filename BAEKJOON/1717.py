import sys

sys.setrecursionlimit(10 ** 9)


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if not a:
        union(b, c)
    if a:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')
