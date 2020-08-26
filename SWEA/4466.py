T = int(input())
for cnt in range(1, T + 1):
    a, b = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr = set(arr)
    arr = sorted(arr, reverse=True)
    total = 0
    for i in range(0, b):
        total += arr[i]
    print('#' + str(cnt) + ' ' + str(total))
