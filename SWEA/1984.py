T = int(input())
for cnt in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop(0)
    arr.pop(-1)
    result = 0
    temp = len(arr)
    for i in arr:
        result += i
    result = round(result/temp)
    print('#' + str(cnt) + ' ' + str(result))