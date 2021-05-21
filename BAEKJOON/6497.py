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


while True:
    graph = []
    answer = 0
    M, N = map(int, sys.stdin.readline().split())
    parents = [i for i in range(M + 1)]
    if M == 0 and N == 0:
        break
    else:
        for i in range(N):
            x, y, z = map(int, sys.stdin.readline().split())
            graph.append([z, x, y])
        graph.sort()
        for z, x, y in graph:
            if find_parent(x) != find_parent(y):
                union_parent(x, y)
            else:
                answer += z
    print(answer)
