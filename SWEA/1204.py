T = int(input())
for cnt in range(1, T + 1):
    num = int(input())
    n = list(map(int, input().split()))
    max_score = 0
    count = 0
    for i in range(100, -1, -1):
        temp = n.count(i)
        if temp > count:
            count = temp
            max_score = i
    print('#' + str(cnt) + ' ' + str(max_score))
