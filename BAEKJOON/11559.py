import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(i, j, color):
    q = deque()
    q.append((i, j))
    chain.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < 12 and 0 <= _y < 6 and visited[_x][_y] == 0 and matrix[_x][_y] == color:
                q.append((_x, _y))
                visited[_x][_y] = 1
                chain.append((_x, _y))


def relocation():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if matrix[j][i] != '.' and matrix[k][i] == '.':
                    matrix[k][i] = matrix[j][i]
                    matrix[j][i] = '.'
                    break


matrix = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(12)]
res = 0
while True:
    flag = False
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                chain = []
                bfs(i, j, matrix[i][j])
                if len(chain) >= 4:
                    flag = True
                    for x, y in chain: matrix[x][y] = '.'
    if not flag: break
    relocation()
    res += 1
print(res)
