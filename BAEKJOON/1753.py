import sys
import heapq
from math import inf

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
dp = [inf] * (V + 1)
heap = []
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

dp[K] = 0
heapq.heappush(heap, (0, K))
while heap:
    weight, now = heapq.heappop(heap)
    for i, j in graph[now]:
        _i = weight + j
        if _i < dp[i]:
            dp[i] = _i
            heapq.heappush(heap, (_i, i))

for i in dp[1:]:
    print(i if i != inf else 'INF')
