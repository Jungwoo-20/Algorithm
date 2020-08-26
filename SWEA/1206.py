T = 10
for cnt in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(2, n - 2):
        temp = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if arr[i] > temp:
            result += arr[i] - temp
    print('#' + str(cnt) + ' ' + str(result))
