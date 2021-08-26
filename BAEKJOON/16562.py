import sys

N, M, k = map(int, sys.stdin.readline().split())
friend = list(map(int, sys.stdin.readline().split()))
matrix = [i for i in range(N+1)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    union_parent(matrix, x, y)
res = 0

visited = set()
for i in range(1, N + 1):
    if i not in visited:
        temp = [i]
        cost = friend[i - 1]
        for j in range(1, N + 1):
            if i != j:
                if find_parent(matrix, i) == find_parent(matrix, j):
                    temp.append(j)
                    cost = min(cost, friend[j - 1])
        visited.update(temp)
        res += cost
if k >= res:
    print(res)
else:
    print('Oh no')