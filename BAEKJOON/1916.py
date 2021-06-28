import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lst = [[] for _ in range(N)]


def bfs_heap(start, end, N, lst):
    queue = []
    dist = [sys.maxsize] * N
    dist[start - 1] = 0
    heapq.heappush(queue, [start - 1, 0])
    while queue:
        point, weight = heapq.heappop(queue)
        for _point, _weight in lst[point]:
            _weight += weight
            if _weight < dist[_point]:
                dist[_point] = _weight
                heapq.heappush(queue, [_point, _weight])
    print(dist[end - 1])


for _ in range(M):
    start, end, weight = list(map(int, sys.stdin.readline().split()))
    lst[start - 1].append([end - 1, weight])
start, end = map(int, sys.stdin.readline().split())

bfs_heap(start, end, N, lst)
