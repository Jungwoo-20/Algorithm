import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
matrix = [[0] * n for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
res = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            matrix[j][k] = 1
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            count = 1
            matrix[i][j] = 1
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for a in range(4):
                    _x = x + dx[a]
                    _y = y + dy[a]
                    if 0 <= _x < m and 0 <= _y < n and matrix[_x][_y] == 0:
                        matrix[_x][_y] = 1
                        count += 1
                        q.append((_x, _y))
            res.append(count)
print(len(res))
res.sort()
print(*res)
