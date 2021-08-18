import sys
from math import inf

N, M = list(map(int, sys.stdin.readline().split()))
arr = [[inf] * M for _ in range(N)]

for i in range(M):
    x, y = list(map(int, sys.stdin.readline().split()))
    arr[x - 1][y - 1] = 1

for k in range(N):
    arr[k][k] = 0
    for i in range(N):
        for j in range(N):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

res = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j] != inf or arr[j][i] != inf:
            cnt += 1
    if cnt == N:
        res += 1
print(res)
