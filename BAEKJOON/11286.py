import sys
import heapq

N = int(sys.stdin.readline())
hp = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        try:
            print(heapq.heappop(hp)[1])
        except:
            print(0)
    else:
        heapq.heappush(hp, (abs(num), num))
