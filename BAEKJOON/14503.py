import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
# d => 0북 1동 2남 3서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 방향 전환 함수
def change(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2


# 후진
def back(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1


def bfs(r, c, d):
    res = 0
    q = deque()
    q.append((r, c, d))
    while q:
        r, c, d = q.popleft()
        # 1
        if matrix[r][c] == 0:
            res += 1
            matrix[r][c] = 2  # 청소 완료
        _d = d
        for i in range(4):
            _d = change(_d)
            _r, _c = r + dy[_d], c + dx[_d]
            if 0 <= _r < N and 0 <= _c < M and matrix[_r][_c] == 0:
                q.append((_r, _c, _d))
                break
            elif i == 3:
                _r, _c = r + dy[back(d)], c + dx[back(d)]
                q.append((_r, _c, d))
                if matrix[_r][_c] == 1:
                    return res


print(bfs(r, c, d))
