N = int(input())

lst = list([[1] * 10])

for _ in range(N):
    lst.append(list([0] * 10))

for i in range(1, N + 1):
    for j in range(0, 10):
        for k in range(j + 1):
            lst[i][j] += lst[i - 1][k]
print(lst[i][9] % 10007)
