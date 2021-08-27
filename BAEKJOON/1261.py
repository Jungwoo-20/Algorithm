import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((0, 0))
visited[0][0] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0 <= _x < N and 0 <= _y < M:
            if visited[_x][_y] == -1:
                if matrix[_x][_y] == 0:
                    visited[_x][_y] = visited[x][y]
                    q.appendleft((_x, _y))
                elif matrix[_x][_y] == 1:
                    visited[_x][_y] = visited[x][y] + 1
                    q.append((_x, _y))

print(visited[N - 1][M - 1])
