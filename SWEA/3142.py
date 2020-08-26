T = int(input())
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = [4, 5, 6, 0, 1, 2, 3]
for cnt in range(1, T + 1):
    sum = 0
    m, d = list(map(int, input().split()))
    for i in range(1, m):
        sum += month[i]
    sum += (d-1)
    print('#' + str(cnt) + ' ' + str(day[sum % 7]))
