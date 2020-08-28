T = int(input())
for cnt in range(1, T + 1):
    d, a, b, f = list(map(int, input().split()))
    result = (d / (a + b)) * f
    print('#' + str(cnt) + ' ' + str(result))
