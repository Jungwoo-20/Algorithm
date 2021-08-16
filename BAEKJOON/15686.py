import sys
from itertools import combinations

N, M = list(map(int, sys.stdin.readline().split()))
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = sys.maxsize
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            house.append((i, j))
        elif matrix[i][j] == 2:
            chicken.append((i, j))

combi = list(combinations(chicken, M))


def solution(com):
    ans = 0
    for x, y in house:  # 집
        tmp = sys.maxsize
        for _x, _y in com:  # 치킨집
            tmp = min(tmp, abs(x - _x) + abs(y - _y))
        ans += tmp
    return ans


for com in combi:
    res = min(res, solution(com))
print(res)
