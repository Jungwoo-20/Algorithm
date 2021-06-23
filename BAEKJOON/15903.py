import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
heapq.heapify(lst)
for _ in range(m):
    hap = heapq.heappop(lst) + heapq.heappop(lst)
    heapq.heappush(lst,hap)
    heapq.heappush(lst,hap)
print(sum(lst))