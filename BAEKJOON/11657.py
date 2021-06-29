import sys

N, M = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N + 1)]
dist = [sys.maxsize for _ in range(N + 1)]


def bellman_ford():
    dist[1] = 0
    for i in range(N):
        for j in range(1, N + 1):
            for edge, weight in lst[j]:
                if dist[j] != sys.maxsize and dist[edge] > weight + dist[j]:
                    dist[edge] = weight + dist[j]
                    if i == N - 1:
                        return True
    return False


for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    lst[A].append([B, C])
res = bellman_ford()
if res:
    print(-1)
else:
    for k in range(2, N + 1):
        if dist[k] == sys.maxsize:
            print(-1)
        else:
            print(dist[k])
