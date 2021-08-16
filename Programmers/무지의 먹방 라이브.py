import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    pre_value = 0
    length = len(food_times)
    while q:
        time = (q[0][0] - pre_value) * length
        if k >= time:
            k -= time
            pre_value, _ = heapq.heappop(q)
            length -= 1
        else:
            idx = k % length
            q.sort(key=lambda x: x[1])
            return q[idx][1]


food = [3, 1, 2]
k = 5
print(solution(food, k))
