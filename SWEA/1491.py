for cnt in range(1, int(input()) + 1):
    n, a, b = list(map(int, input().split()))
    result = []
    for i in range(1, n):
        for j in range(1, n):
            if j <= i:
                if i * j <= n:
                    if a * abs(i - j) + b * (n - i * j) >= 0:
                        result.append(a * abs(i - j) + b * (n - i * j))
    print('#' + str(cnt) + ' ' + str(min(result)))