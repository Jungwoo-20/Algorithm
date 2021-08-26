import sys

TC = int(sys.stdin.readline())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(TC):
    dist = list(map(str, sys.stdin.readline().rstrip()))
    go = 0  # 0북1동2남3서
    start_x, start_y = 0, 0
    trace = [(start_x, start_y)]
    for i in dist:
        if i == 'F':
            start_x += dx[go]
            start_y += dy[go]
        elif i == 'B':
            start_x -= dx[go]
            start_y -= dy[go]
        elif i == 'L':
            if go == 0:
                go = 3
            else:
                go -= 1
        elif i == 'R':
            if go == 3:
                go = 0
            else:
                go += 1
        trace.append((start_x, start_y))
    width = max(trace, key=lambda x: x[0])[0] - min(trace, key=lambda x: x[0])[0]
    height = max(trace, key=lambda x: x[1])[1] - min(trace, key=lambda x: x[1])[1]
    print(width * height)
