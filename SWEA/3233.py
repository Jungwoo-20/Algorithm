T = int(input())
for cnt in range(1, T + 1):
    n,m = list(map(int, input().split()))
    result = (n**2)//(m**2)
    print('#' + str(cnt) + ' ' + str(result))
