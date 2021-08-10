import sys
N = int(sys.stdin.readline())
T, P = [], []
dp = [0] * (N + 1)

for i in range(N):
    info = list(map(int, sys.stdin.readline().split()))
    T.append(info[0])
    P.append(info[1])
tmp = 0
for i in range(0, N):
    tmp = max(tmp, dp[i])
    if T[i] + i > N:
        continue
    dp[i + T[i]] = max(tmp + P[i], dp[i + T[i]])

print(max(dp))
