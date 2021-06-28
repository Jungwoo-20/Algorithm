import sys
import heapq

N, M, X = list(map(int, sys.stdin.readline().split()))
lst = [[] for _ in range(N)]
R_lst = [[] for _ in range(N)]
dist = [sys.maxsize] * N
R_dist = [sys.maxsize] * N


def bfs_heap(start, lst, dist):
    queue = []
    dist[start - 1] = 0
    heapq.heappush(queue, [start - 1, 0])
    while queue:
        point, weight = heapq.heappop(queue)
        if dist[point] < weight:
            continue
        for _point, _weight in lst[point]:
            _weight += weight
            if _weight < dist[_point]:
                dist[_point] = _weight
                heapq.heappush(queue, [_point, _weight])
    return dist


for _ in range(M):
    start, end, weight = list(map(int, sys.stdin.readline().split()))
    lst[start - 1].append([end - 1, weight])
    R_lst[end - 1].append([start - 1, weight])

dist = bfs_heap(X, lst, dist)
R_dist = bfs_heap(X, R_lst, R_dist)
res = 0
for i, j in zip(dist, R_dist):
    res = max(res, i + j)
print(res)
