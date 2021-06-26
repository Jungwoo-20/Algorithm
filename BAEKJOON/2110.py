import sys

N, C = map(int, sys.stdin.readline().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()

start = 1
end = house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    setting = house[0]
    for i in house:
        if mid + setting <= i:
            cnt += 1
            setting = i
    if cnt >= C:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)
