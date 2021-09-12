import sys

n, m = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    matrix.append(list(map(int, tmp)))
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
res = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if matrix[i - 1][j - 1] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if dp[i][j] > res:
                res = dp[i][j]
print(res ** 2)
