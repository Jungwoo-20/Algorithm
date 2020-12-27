import sys

sys.setrecursionlimit(10000)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = []

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])

while queue:
    row, col = queue.pop(0)
    for i in range(4):
        Trow = row + dx[i]
        Tcol = col + dy[i]

        if 0 <= Trow < N and 0 <= Tcol < M and tomato[Trow][Tcol] == 0:
            tomato[Trow][Tcol] = tomato[row][col] + 1
            queue.append([Trow, Tcol])

flag = False
res = -3

for i in tomato:
    for j in i:
        if j == 0:
            flag = True
        res = max(res, j)

if flag:
    print(-1)
elif res == -1:
    print(0)
else:
    print(res - 1)
