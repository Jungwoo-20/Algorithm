import sys

sys.setrecursionlimit(10 ** 9)


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


N = int(sys.stdin.readline())
graph_x = []
graph_y = []
graph_z = []
_graph = []
parents = [i for i in range(N)]
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    graph_x.append([x, i])
    graph_y.append([y, i])
    graph_z.append([z, i])
graph_x.sort()
graph_y.sort()
graph_z.sort()

for i in range(N - 1):
    _graph.append((abs(graph_x[i + 1][0] - graph_x[i][0]), graph_x[i][1], graph_x[i + 1][1]))
    _graph.append((abs(graph_y[i + 1][0] - graph_y[i][0]), graph_y[i][1], graph_y[i + 1][1]))
    _graph.append((abs(graph_z[i + 1][0] - graph_z[i][0]), graph_z[i][1], graph_z[i + 1][1]))
_graph.sort()
res = 0
for w, x, y in _graph:
    if find_parent(x) != find_parent(y):
        res += w
        union_parent(x, y)

print(res)
