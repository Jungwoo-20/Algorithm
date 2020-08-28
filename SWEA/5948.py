T = int(input())
for cnt in range(1, T + 1):
    arr = list(map(int, input().split()))
    result_arr = []
    for i in range(7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                result_arr.append(arr[i] + arr[j] + arr[k])
    result_arr = set(result_arr)
    result_arr = sorted(result_arr, reverse=True)
    print('#' + str(cnt) + ' ' + str(result_arr[4]))
