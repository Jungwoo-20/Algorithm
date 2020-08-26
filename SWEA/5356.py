T = int(input())
for cnt in range(1, T + 1):
    arr = []
    result = ''
    for i in range(5):
        arr1 = input()
        arr.append(list(arr1))
    max_len = 0
    for i in range(5):
        max_len = max(max_len, len(arr[i]))
    for i in range(max_len):
        for j in range(5):
            if (len(arr[j]) > i):
                result += arr[j][i]
    print('#' + str(cnt) + ' ' + str(result))