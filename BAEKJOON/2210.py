import sys

lst = []
res = []


def dfs(i, j, num):
    if len(num) == 6:
        if num not in res:
            res.append(num)
        return
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(4):
        _dx = dx[x] + i
        _dy = dy[x] + j
        if 0 <= _dx < 5 and 0 <= _dy < 5:
            dfs(_dx, _dy, num + lst[_dx][_dy])


for i in range(5):
    lst.append(list(map(str, sys.stdin.readline().split())))

for i in range(5):
    for j in range(5):
        dfs(i, j, lst[i][j])
print(len(res))
