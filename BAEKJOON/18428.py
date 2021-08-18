import sys
from itertools import combinations

N = int(sys.stdin.readline())
matrix = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
empty = []
teacher = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'X':
            empty.append((i, j))
        elif matrix[i][j] == 'T':
            teacher.append((i, j))


def check():
    for tea in teacher:
        x, y = tea
        # 상
        _x, _y = x, y
        while _x > 0:
            _x -= 1
            if matrix[_x][_y] == 'S':
                return False
            if matrix[_x][_y] == 'O':
                break
        # 하
        _x, _y = x, y
        while _x < N - 1:
            _x += 1
            if matrix[_x][_y] == 'S':
                return False
            if matrix[_x][_y] == 'O':
                break
        # 좌
        _x, _y = x, y
        while _y > 0:
            _y -= 1
            if matrix[_x][_y] == 'S':
                return False
            if matrix[_x][_y] == 'O':
                break
        # 우
        _x, _y = x, y
        while _y < N - 1:
            _y += 1
            if matrix[_x][_y] == 'S':
                return False
            if matrix[_x][_y] == 'O':
                break
    return True


for wall in combinations(empty, 3):
    for i in wall:
        x, y = i
        matrix[x][y] = 'O'
    if check():
        print('YES')
        break
    for i in wall:
        x, y = i
        matrix[x][y] = 'X'
else:
    print('NO')
