import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
p = [i for i in range(n + 1)]
g = []


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        p[y] = x
    else:
        p[x] = y


def distance(x, y):
    return ((x[0] - y[0]) ** 2 + abs(x[1] - y[1]) ** 2) ** 0.5


lst = [[]]
lst2 = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])

line = n - 1
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if find(x) != find(y):
        union(x, y)
        line -= 1

for i in range(1, n):
    for j in range(1 + i, n + 1):
        dist = distance(lst[i], lst[j])
        heapq.heappush(lst2, [dist, i, j])
res = 0
while line:
    dist, x, y = heapq.heappop(lst2)
    if find(x) != find(y):
        union(x, y)
        res += dist
        line -= 1
print('%0.2f' % res)
