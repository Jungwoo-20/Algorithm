from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < n and 0 <= _y < m and maps[_x][_y] == 1 and visited[_x][_y] == -1:
                q.append((_x, _y))
                visited[_x][_y] = visited[x][y] + 1
    return visited[-1][-1]


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))
