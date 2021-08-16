import sys

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            sys.exit()
        cnt = lst[i][j]  # 현재 위치에서 이동할 수 있는 거리
        if cnt + j < N:
            dp[i][cnt + j] += dp[i][j]
        if cnt + i < N:
            dp[cnt + i][j] += dp[i][j]
