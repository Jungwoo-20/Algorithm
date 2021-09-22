import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
day = 0
res = []


def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    check = 0
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < n and 0 <= _y < m and not visited[_x][_y]:
                if matrix[_x][_y] == 0:
                    visited[_x][_y] = True
                    q.append((_x, _y))
                elif matrix[_x][_y] == 1:
                    visited[_x][_y] = True
                    matrix[_x][_y] = 0
                    check += 1
    res.append(check)
    return check


while True:
    if bfs() == 0:
        break
    day += 1
print(day)
print(res[-2])
