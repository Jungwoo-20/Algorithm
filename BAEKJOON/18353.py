import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = [1] * N
for i in range(N):
    for j in range(len(arr[:i])):
        if arr[i] < arr[j] and res[i] < res[j] + 1:
            res[i] = res[j] + 1
print(N-max(res))
