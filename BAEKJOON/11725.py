import sys

sys.setrecursionlimit(10 ** 7)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def DFS(start, tree, parent):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            DFS(i, tree, parent)


DFS(1, tree, parent)

for i in range(2, n + 1):
    print(parent[i])
