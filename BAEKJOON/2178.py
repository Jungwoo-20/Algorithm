import sys

N, M = map(int, sys.stdin.readline().split())
lst = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    lst.append(list(sys.stdin.readline().rstrip()))

queue = [[0, 0]]
lst[0][0] = 1
while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0 <= _x < N and 0 <= _y < M and lst[_x][_y] == '1':
            queue.append([_x, _y])
            lst[_x][_y] = lst[x][y] + 1
print(lst[N - 1][M - 1])
