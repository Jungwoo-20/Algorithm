T = int(input())
for cnt in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = []
    temp = []
    for tmp in range(N):
        arr.append(list(map(int, input().split())))
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            num = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    num += int(arr[k][l])
            temp.append(num)
    print('#' + str(cnt) + ' ' + str(max(temp)))