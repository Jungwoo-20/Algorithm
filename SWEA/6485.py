for cnt in range(1, int(input()) + 1):
    n = int(input())
    dic = {}
    for i in range(5001):
        dic[i] = 0
    for i in range(n):
        a,b = list(map(int, input().split()))
        for j in range(a,b+1):
            dic[j] +=1
    temp = int(input())
    result = []
    for i in range(temp):
        result.append(dic[int(input())])
    print('#' + str(cnt),end=' ')
    print(*result)
