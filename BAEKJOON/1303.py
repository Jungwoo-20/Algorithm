import sys
from collections import deque


def bfs(teamColor, x, y):
    power = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < M and 0 <= _y < N and graph[_x][_y] == teamColor and not visited[_x][_y]:
                power += 1
                visited[_x][_y] = True
                q.append((_x, _y))
    return power


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = list(map(int, sys.stdin.readline().split()))
graph = [list(sys.stdin.readline()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

white, blue = 0, 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W' and not visited[i][j]:
            white += bfs('W', i, j) ** 2
        elif graph[i][j] == 'B' and not visited[i][j]:
            blue += bfs('B', i, j) ** 2

print(white, blue)
