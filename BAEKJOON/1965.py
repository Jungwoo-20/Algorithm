from bisect import bisect_left
import sys

n = int(input())
matrix = list(map(int, sys.stdin.readline().split()))
dp = []

for i in matrix:
    if not dp or dp[-1] < i:
        dp.append(i)
    else:
        dp[bisect_left(dp, i)] = i

print(len(dp))
