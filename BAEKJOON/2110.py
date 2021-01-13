N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()

start = 1
end = house[-1] - house[0]
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    setting = house[0]
    for i in range(1, N):
        if setting + mid <= house[i]:
            cnt += 1
            setting = house[i]
    if cnt >= C:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)
