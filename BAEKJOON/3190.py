import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
matrix = [[0] * N for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(K):
    tmpx, tmpy = list(map(int, sys.stdin.readline().split()))
    matrix[tmpx - 1][tmpy - 1] = 1

L = int(sys.stdin.readline())
change = []
for i in range(L):
    t, tmp = sys.stdin.readline().split()
    change.append((int(t), tmp))


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def solution():
    x, y = 0, 0
    matrix[x][y] = 99
    direction = 0
    time = 0
    index = 0
    q = deque()
    q.append((x, y))
    while q:
        _x = x + dx[direction]
        _y = y + dy[direction]
        if 0 <= _x < N and 0 <= _y < N and matrix[_x][_y] != 99:
            if matrix[_x][_y] == 0:
                matrix[_x][_y] = 99
                q.append((_x, _y))
                tx, ty = q.popleft()
                matrix[tx][ty] = 0
            if matrix[_x][_y] == 1:
                matrix[_x][_y] = 99
                q.append((_x, _y))
        else:
            time += 1
            break
        x, y = _x, _y
        time += 1
        if index < L and time == change[index][0]:
            direction = turn(direction, change[index][1])
            index += 1
    return time


print(solution())
