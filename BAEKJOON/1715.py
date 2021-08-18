import sys
import heapq

N = int(sys.stdin.readline())
q = []
for _ in range(N): heapq.heappush(q, int(sys.stdin.readline()))

if len(q) == 1:
    print(0)
else:
    res = 0
    while len(q) > 1:
        low = heapq.heappop(q)
        high = heapq.heappop(q)
        res += low + high
        heapq.heappush(q, low+high)
    print(res)
