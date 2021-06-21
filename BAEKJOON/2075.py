import heapq
import sys

N = int(sys.stdin.readline())
res = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    if not res:
        for j in tmp:
            heapq.heappush(res, j)
    else:
        for j in tmp:
            if res[0] < j:
                heapq.heappush(res, j)
                heapq.heappop(res)
print(res[0])