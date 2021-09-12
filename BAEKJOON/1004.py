import sys

TC = int(sys.stdin.readline())
for _ in range(TC):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    cnt = 0
    for _ in range(N):
        cx, cy, r = map(int, sys.stdin.readline().split())
        x = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
        y = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** 0.5
        if (x < r and y > r) or (x > r and y < r):
            cnt += 1
    print(cnt)
