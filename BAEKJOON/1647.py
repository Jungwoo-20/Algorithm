import sys


def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


V, E = map(int, sys.stdin.readline().split())
graph = []
for i in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph.append([C, A, B])
parents = [0] * (V + 1)
for i in range(1, V + 1):
    parents[i] = i
# Weight 정렬
graph.sort()
result = []
ans = 0
for W, A, B in graph:
    if find_parent(A) != find_parent(B):
        union_parent(A, B)
        ans += W
        result.append(W)
ans -= result.pop()

print(ans)
