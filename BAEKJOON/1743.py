import sys
from collections import deque

N, M, K = list(map(int, sys.stdin.readline().split()))
graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for i in range(K):
    x, y = list(map(int, sys.stdin.readline().split()))
    graph[x - 1][y - 1] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < M and graph[_x][_y] and not visited[_x][_y]:
                cnt += 1
                visited[_x][_y] = True
                q.append((_x, _y))
    return cnt


res = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            res.append(bfs(i, j))
print(max(res))
