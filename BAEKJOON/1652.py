n = int(input())

room = []
row = 0
col = 0
for i in range(n):
    room.append(list(str(input())))

for i in range(n):
    cnt = 0
    for j in range(n):
        if room[i][j] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            row += 1
for i in range(n):
    cnt = 0
    for j in range(n):
        if room[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            col += 1
print(row, end=' ')
print(col)
