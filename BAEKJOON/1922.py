import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

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


arr = []
parents = [i for i in range(N + 1)]
result = 0
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append([c, a, b])
arr.sort()
for c, a, b in arr:
    if find(a) != find(b):
        union(a, b)
        result += c
print(result)
