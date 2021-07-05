import sys
import heapq

t = int(sys.stdin.readline())
visited = [0] * 1000000


def clean(q):
    while q and visited[q[0][1]] == 0:
        heapq.heappop(q)


for _ in range(t):
    min_heap = []
    max_heap = []
    k = int(sys.stdin.readline())
    size = 0
    for i in range(k):
        a, n = map(str, sys.stdin.readline().split())
        n = int(n)
        if a == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visited[i] = 1
        else:
            if n == 1:
                clean(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
            else:
                clean(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

    clean(max_heap)
    clean(min_heap)
    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
