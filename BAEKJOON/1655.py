import sys
import heapq

N = int(sys.stdin.readline())
left, right = [], []

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, -num)  # 최대 힙 구성
    else:
        heapq.heappush(right, num)  # 최소 힙 구성

    if right and -left[0] > right[0]:
        heapq.heappush(left, -heapq.heappop(right))
        heapq.heappush(right, -heapq.heappop(left))

    print(-left[0])