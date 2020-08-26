T = int(input())
for cnt in range(1, T + 1):
    n, a, b = list(map(int, input().split()))
    maxn = b if a > b else a
    minn = a + b - n if a + b > n else 0
    print('#' + str(cnt) + ' ' + str(maxn)+ ' ' + str(minn))
