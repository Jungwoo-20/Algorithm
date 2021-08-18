import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))
matrix = []
virus_data = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if matrix[i][j] != 0:
            virus_data.append([matrix[i][j], 0, i, j])
virus_data.sort()
q = deque(virus_data)
S, X, Y = list(map(int, sys.stdin.readline().split()))
while q:
    virus, time, x, y = q.popleft()
    if time == S:
        break
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0 <= _x < N and 0 <= _y < N and matrix[_x][_y] == 0:
            matrix[_x][_y] = virus
            q.append((virus, time + 1, _x, _y))
print(matrix[X - 1][Y - 1])
