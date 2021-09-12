import sys

x, y = map(int, sys.stdin.readline().split())
z = int((y*100) / x)
if z >= 99:
    print(-1)
else:
    left, right = 0, 1000000000
    while left <= right:
        mid = (left + right) // 2
        _x = x + mid
        _y = y + mid
        if int((_y*100) / _x) > z:
            right = mid - 1
        else:
            left = mid + 1
    print(right + 1)
