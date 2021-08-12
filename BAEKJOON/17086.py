import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]
cnt = 0
dist = 0


def bfs(x, y):
    global cnt
    q = deque()
    tmp = 0
    cnt += 1
    visited[x][y] = cnt
    q.append((x, y))
    while q:
        tmp += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(8):
                _x = x + dx[i]
                _y = y + dy[i]
                if 0 <= _x < N and 0 <= _y < M and visited[_x][_y] < cnt:
                    if lst[_x][_y] == 1:
                        return tmp
                    else:
                        q.append((_x, _y))
                        visited[_x][_y] = cnt
    return tmp - 1


for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            dist = max(dist, bfs(i, j))
print(dist)
