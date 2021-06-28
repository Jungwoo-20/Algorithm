import sys
import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_heap(queue, cnt):
    while queue:
        w, x, y = heapq.heappop(queue)
        for i in range(4):
            _dx = dx[i] + x
            _dy = dy[i] + y
            if 0 <= _dx < N and 0 <= _dy < N and visited[_dx][_dy] == 0 and money[_dx][_dy] > w + lst[_dx][_dy]:
                money[_dx][_dy] = w + lst[_dx][_dy]
                visited[_dx][_dy] = 1
                heapq.heappush(queue, [money[_dx][_dy], _dx, _dy])
    print('Problem {0}: {1}'.format(cnt, money[N - 1][N - 1]))


cnt = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    lst = []
    for _ in range(N):
        lst.append(list(map(int, sys.stdin.readline().split())))
    money = [[sys.maxsize] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    queue = [[lst[0][0], 0, 0]]
    bfs_heap(queue, cnt)
    cnt += 1
