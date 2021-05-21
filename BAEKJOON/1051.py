import sys

arr = []
N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))

_tmp = min(N, M)
res = 0
for i in range(N):
    for j in range(M):
        for k in range(_tmp):
            if i + k < N and j + k < M:
                if arr[i][j] == arr[i][j + k] and arr[i][j] == arr[i + k][j] and arr[i][j] == arr[i + k][j + k] and res < k:
                    res = k
print((res+1)**2)