import sys

N, M = list(map(int, sys.stdin.readline().split()))
A = [0] + list(map(int, sys.stdin.readline().split()))
C = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(sum(C) + 1)] for _ in range(N + 1)]
res = sum(C)
for i in range(1, N + 1):
    byte = A[i]
    cost = C[i]
    for j in range(1, sum(C) + 1):
        if j < cost:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(byte + dp[i - 1][j - cost], dp[i - 1][j])
        if dp[i][j] >= M:
            res = min(res, j)

if M!=0:
    print(res)
else:
    print(0)
