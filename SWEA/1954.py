T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    x, y = 0, 0
    dist = 0
    matrix[x][y] = 1
    for i in range(2, (N ** 2) + 1):
        x += dx[dist]
        y += dy[dist]
        matrix[x][y] = i
        if 0 <= x + dx[dist] < N and 0 <= y + dy[dist] < N and matrix[x + dx[dist]][y + dy[dist]] == 0:
            continue
        if dist != 3:
            dist += 1
        else:
            dist = 0
    print('#' + str(t))
    for m in matrix:
        print(*m)

