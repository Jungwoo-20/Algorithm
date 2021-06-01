import sys
from math import inf

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

res = [[inf] * n for _ in range(n)]
# 이동비용 배열
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    res[a - 1][b - 1] = min(res[a - 1][b - 1], c)

# 플로이드 와샹 알고리즘
for k in range(n):
    res[k][k] = 0
    for i in range(n):
        for j in range(n):
            res[i][j] = min(res[i][j], res[i][k] + res[k][j])

for i in res:
    for j in range(n):
        if i[j] == inf:
            i[j] = 0
        print(i[j], end=' ')
    print()
