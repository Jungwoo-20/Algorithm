import sys
from collections import deque

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            start_x, start_y = i, j  # 아기상어 시작점
            matrix[i][j] = 0
            break

size = 2  # 아기상어 초기 크기
move_cnt = 0
eat = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while True:
    q = deque()
    q.append((start_x, start_y, 0))
    visited = [[False] * N for _ in range(N)]
    flag = 1e10
    fish = []
    while q:
        x, y, cnt = q.popleft()
        if cnt > flag:
            break
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if _x < 0 or _x >= N or _y < 0 or _y >= N or matrix[_x][_y] > size or visited[_x][_y]:
                continue
            if matrix[_x][_y] < size and matrix[_x][_y] != 0:
                fish.append((_x, _y, cnt + 1))
                flag = cnt
            q.append((_x, _y, cnt + 1))
            visited[_x][_y] = True
    if len(fish) > 0:
        fish.sort()
        x, y, cnt = fish[0][0], fish[0][1], fish[0][2]
        move_cnt += cnt
        eat += 1
        matrix[x][y] = 0
        if eat == size:
            size += 1
            eat = 0
        start_x, start_y = x, y
    else:
        break
print(move_cnt)
