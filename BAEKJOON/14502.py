import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0


def bfs():
    global res
    cnt = 0
    q = deque()
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            visited[i][j] = matrix[i][j]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < M:
                if visited[_x][_y] == 0:
                    visited[_x][_y] = 2
                    q.append((_x, _y))
    for i in visited:
        for j in i:
            if j == 0:
                cnt += 1
    res = max(cnt, res)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                make_wall(cnt + 1)
                matrix[i][j] = 0


make_wall(0)
print(res)
