import sys

dw = [1, 0, -1, 0, 1, 1, -1, -1]
dh = [0, 1, 0, -1, -1, 1, -1, 1]


def bfs(i, j):
    lst[i][j] = 0
    queue = [[i, j]]
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(8):
            a = x + dw[i]
            b = y + dh[i]
            if 0 <= a < h and 0 <= b < w and lst[a][b]:
                lst[a][b] = 0
                queue.append([a, b])


while True:
    res = 0
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    lst = []
    for i in range(h):
        lst.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1:
                print(lst[i][j])
                res+=1
                bfs(i, j)
    print(res)
