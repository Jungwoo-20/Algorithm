import heapq


def solution(n, works):
    answer = 0
    heap = []
    if n >= sum(works):
        return 0
    for work in works:
        heapq.heappush(heap, (-work, work))
    while True:
        if n == 0:
            break
        work = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, (-work, work))
        n -= 1

    for i in heap:
        if i[1] <= 0:
            continue
        answer += (i[1] ** 2)
    return answer
