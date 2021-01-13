import sys

sys.setrecursionlimit(10 ** 7)


def find(x):
    if parents[x] == x:
        return x
    else:
        return find(parents[x])


def union(x, y):
    if find(x) != find(y):
        parents[find(x)] = y


N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')
