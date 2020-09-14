for cnt1 in range(1, int(input()) + 1):
    arr = list(map(int, input()))
    cnt = 0
    result = 0
    for i in range(len(arr)):
        while True:
            if cnt < i:
                cnt += 1
                result += 1
            else:
                cnt += arr[i]
                break
    print('#' + str(cnt1) + ' ' + str(result))
