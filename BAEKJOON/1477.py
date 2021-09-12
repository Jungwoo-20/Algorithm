import sys

N, M, L = map(int, sys.stdin.readline().split())
road = list(map(int, sys.stdin.readline().split()))
road.append(0)
road.append(L - 1)
road = sorted(road)
start, end = 0, L - 1
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(len(road)):
        if road[i] - road[i - 1] > mid:
            cnt += (road[i] - road[i - 1] - 1) // mid

    if cnt > M:
        start = mid + 1
    else:
        res = mid
        end = mid - 1
print(res)
