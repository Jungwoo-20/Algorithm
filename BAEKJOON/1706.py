n, m = list(map(int, input().split()))
room = []
row = 0
col = 0
for i in range(n):
    room.append(list(str(input())))

mun = []

for i in range(n):
    cnt = 0
    tmp = ''
    for j in range(m):
        if room[i][j] != '#':
            tmp += room[i][j]
            cnt += 1
        else:
            if cnt >= 2:
                mun.append(tmp)
                tmp = ''
                cnt = 0
            else:
                tmp = ''
                cnt = 0
    if cnt >= 2:
        mun.append(tmp)
for i in range(m):
    cnt = 0
    tmp = ''
    for j in range(n):
        if room[j][i] != '#':
            tmp += room[j][i]
            cnt += 1
        else:
            if cnt >= 2:
                mun.append(tmp)
                tmp = ''
                cnt = 0
            else:
                tmp = ''
                cnt = 0
    if cnt >= 2:
        mun.append(tmp)
res = sorted(mun)
print(res[0])
