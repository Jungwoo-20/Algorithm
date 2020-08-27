T = int(input())
for cnt in range(1, T + 1):
    result = 0
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    avg = sum(arr) // n
    for i in range(n):
        result += abs(arr[i] - avg)
    print('#' + str(cnt) + ' ' + str(result // 2))
