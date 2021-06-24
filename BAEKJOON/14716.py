import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
cnt = 0
x_y = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]


def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for k in range(8):
            _y = y + x_y[k][0]
            _x = x + x_y[k][1]
            if (0 <= _y < M) and (0 <= _x < N) and visited[_y][_x] == 0 and lst[_y][_x] == 1:
                visited[_y][_x] = 1
                q.append([_y, _x])


for i in range(M):
    for j in range(N):
        if lst[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            bfs(i, j)
print(cnt)
