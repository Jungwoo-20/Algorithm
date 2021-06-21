import heapq


def solution(scoville, K):
    res = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + (2 * heapq.heappop(scoville)))
        except:
            return -1
        res += 1
    return res


sc = [1, 2, 3, 9, 10, 12]
print(solution(sc, 7))
