import sys
import heapq

N, M, K = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N + 1)]
dist = [[sys.maxsize for _ in range(K + 1)] for _ in range(N + 1)]
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    matrix[x].append((z, y))
    matrix[y].append((z, x))


def solution(n):
    q = []
    cnt = 0
    dist[n][cnt] = 0
    heapq.heappush(q, (0, n, cnt))
    while q:
        wei, end, cnt = heapq.heappop(q)
        if dist[end][cnt] < wei:
            continue
        for w, idx in matrix[end]:
            _w = w + wei
            if dist[idx][cnt] > _w:
                dist[idx][cnt] = _w
                heapq.heappush(q, (_w, idx, cnt))
            if cnt < K and dist[idx][cnt + 1] > wei:
                dist[idx][cnt + 1] = wei
                heapq.heappush(q, (wei, idx, cnt + 1))


solution(1)
print(min(dist[N]))
