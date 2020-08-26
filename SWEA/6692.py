T = int(input())
for cnt in range(1, T + 1):
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = list(map(float, input().split()))
        sum += a*b
    print('#' + str(cnt) + ' ' + str(sum))
