import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
start, end = 0, max(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in arr:
        total += min(i, mid)
    if total <= M:
        start = mid + 1
    else:
        end = end - 1
print(end)