T = int(input())
for cnt in range(1, T + 1):
    n, q = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append([i + 1, 0])
    for i in range(q):
        l, r = list(map(int, input().split()))
        for j in arr:
            if l <= j[0] <= r:
                j[1] = i + 1
    print('#' + str(cnt), end=' ')
    for i in arr:
        print(i[1], end=' ')
    print()
