T = 10
for cnt in range(1, T + 1):
    a, arr = input().split()
    result = ''
    for i in arr:
        if len(result) > 0 and result[-1] == i:
            result = result[:-1]
        else:
            result += i
    print('#' + str(cnt) + ' ' + str(result))