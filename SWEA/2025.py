n = int(input())

for i in range(n):
    m = int(input())
    ans = [[1]]

    for j in range(1, m):
        tmp = []
        for k in range(j + 1):
            if k == 0 or k == j:
                tmp.append(1)
            else:
                tmp.append(ans[j - 1][k - 1] + ans[j - 1][k])
        ans.append(tmp)

    print("#" + str(i + 1))
    for line in ans:
        print(' '.join(map(str, line)))