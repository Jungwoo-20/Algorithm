T = 10
for cnt in range(1, T + 1):
    n = int(input())
    lst = []
    result = []
    for i in range(100):
        arr = list(map(int, input().split()))
        lst.append(arr)
    for i in range(len(lst)):
        sum = 0
        for j in range(len(lst)):
            sum += lst[i][j]
        result.append(sum)
    for i in range(len(lst)):
        sum = 0
        for j in range(len(lst)):
            sum += lst[j][i]
        result.append(sum)
    sum = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                sum += lst[i][j]
    result.append(sum)
    sum = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == len(lst) - j:
                sum += lst[i][j]
    result.append(sum)
    print('#' + str(cnt) + ' ' + str(max(result)))
