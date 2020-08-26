T = int(input())
for cnt in range(1, T + 1):
    a, b, c = list(map(int, input().split()))
    min_x = min(a, b)
    print('#' + str(cnt) + ' ' + str(int(c/min_x)))
