import sys

sys.setrecursionlimit(10 ** 9)


def find(x):
    if parents[x] == x:
        return x
    p = find(parents[x])
    parents[x] = p
    return p


def union(x, y):
    if find(x) != find(y):
        parents[find(y)] = x


def find_parent(x):
    if parents[x] == x:
        return x
    return find_parent(parents[x])


N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if not a:
        union(b, c)
    if a:
        if find_parent(b) == find_parent(c):
            print('YES')
        else:
            print('NO')
