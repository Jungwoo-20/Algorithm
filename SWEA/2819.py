T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(cnt, i, j, num):
    if cnt == 7:
        res.append(num)
        return
    for k in range(4):
        _i = i + dx[k]
        _j = j + dy[k]
        if 0 <= _i < 4 and 0 <= _j < 4:
            bfs(cnt + 1, _i, _j, num + matrix[_i][_j])


for t in range(1, T + 1):
    res = []
    matrix = [list(map(str, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            bfs(0, i, j, '')
    res = set(res)
    print('#' + str(t) + ' ' + str(len(res)))
