import sys
import heapq

N = int(sys.stdin.readline())
hp = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if hp:
            print(heapq.heappop(hp)[1])
        else:
            print(0)
    else:
        heapq.heappush(hp, [-num, num])
