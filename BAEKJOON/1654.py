import sys

K, N = map(int, sys.stdin.readline().split())
arr = []
for _ in range(K):
    arr.append(int(sys.stdin.readline()))

start = 0
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in arr:
        lines += i // mid
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
