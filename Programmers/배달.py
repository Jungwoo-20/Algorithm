from collections import deque
import sys


def bfs(start, cost, matrix, N, K):
    q = deque()
    q.append((start, cost))
    dist = [sys.maxsize] * (N + 1)
    dist[1] = 0
    while q:
        info_start, info_cost = q.popleft()
        for i in matrix[info_start]:
            info_end, info_end_cost = i[0], i[1]
            if info_cost + info_end_cost <= K and info_cost + info_end_cost < dist[info_end]:
                dist[info_end] = info_cost + info_end_cost
                q.append((info_end, info_cost + info_end_cost))
    return dist


def solution(N, road, K):
    answer = 0
    matrix = [[] for _ in range(N + 1)]
    for start, end, dist in road:
        matrix[start].append([end, dist])
        matrix[end].append([start, dist])
    dist = bfs(1, 0, matrix, N, K)
    for i in dist:
        if i != sys.maxsize:
            answer += 1

    return answer


N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3

print(solution(N, road, K))
