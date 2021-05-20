import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
visited = [0] * (V + 1)
tree = [[] for _ in range(V + 1)]
heap = [[0, 1]]

for i in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    tree[start].append([weight, end])
    tree[end].append([weight, start])

ans = 0
cnt = 0
while heap:
    if cnt == V:
        break
    weight, start = heapq.heappop(heap)
    if not visited[start]:
        visited[start] = 1
        ans += weight
        cnt += 1
        for i in tree[start]:
            heapq.heappush(heap, i)
print(ans)
