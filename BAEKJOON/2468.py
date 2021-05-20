import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N = int(sys.stdin.readline())
home = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def bfs(j, k):
    queue = deque()
    queue.append([j, k])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            _x = dx[i] + x
            _y = dy[i] + y
            if 0 <= _x < N and 0 <= _y < N and rain[_x][_y] == 0:
                rain[_x][_y] = 1
                queue.append([_x,_y])


result = 0
for i in range(0, 101):
    rain = [[0] * N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if home[j][k] <= i:
                rain[j][k] = 1
    for j in range(N):
        for k in range(N):
            if rain[j][k] == 0:
                rain[j][k] = 1
                bfs(j, k)
                cnt += 1
    if cnt == 0:
        break
    result = max(result, cnt)
print(result)
