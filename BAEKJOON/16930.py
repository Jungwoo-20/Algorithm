import sys
from collections import deque

N, M, K = list(map(int, sys.stdin.readline().split()))
lst = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
start_x, start_y, end_x, end_y = list(map(int, sys.stdin.readline().split()))
visited[start_x - 1][start_y - 1] = 0
q = deque()
q.append((start_x - 1, start_y - 1))

while q:
    y, x = q.popleft()
    if y == end_x - 1 and x == end_y - 1:
        print(visited[y][x])
        sys.exit()
    for i in range(4):
        for dist in range(1, K + 1):
            _x = x + dx[i] * dist
            _y = y + dy[i] * dist
            if _x < 0 or _x >= M or _y < 0 or _y >= N:
                break
            if lst[_y][_x] == '#':
                break
            if visited[_y][_x] == -1:
                visited[_y][_x] = visited[y][x] + 1
                q.append((_y, _x))
            elif visited[_y][_x] == visited[y][x] + 1:
                continue
            else:
                break
print(-1)
