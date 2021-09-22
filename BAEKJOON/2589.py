import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
matrix = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(i, j):
    cnt = 0
    visited = [[0] * c for _ in range(r)]
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for a in range(4):
            _x = x + dx[a]
            _y = y + dy[a]
            if 0 <= _x < r and 0 <= _y < c and not visited[_x][_y] and matrix[_x][_y] == 'L':
                q.append((_x, _y))
                visited[_x][_y] = visited[x][y] + 1
                cnt = max(cnt, visited[_x][_y])
    return cnt-1


res = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'L':
            res = max(res, bfs(i, j))
print(res)
