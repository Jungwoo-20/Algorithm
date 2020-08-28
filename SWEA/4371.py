T = int(input())
for cnt in range(1, T + 1):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(int(input())-1)
    del arr[0]
    for i in arr:
        arr = set(arr)
        arr -= set(range(i * 2, max(arr) + 1, i))
    print('#' + str(cnt) + ' ' + str(len(arr)))
