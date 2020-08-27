T = int(input())
for cnt in range(1, T + 1):
    d, h, m = list(map(int, input().split()))
    tmp = 11 * 60 * 24 + 11 * 60 + 11
    temp = d * 60 * 24 + h * 60 + m
    result = temp - tmp
    if result < 0:
        result = -1
    print('#' + str(cnt) + ' ' + str(result))