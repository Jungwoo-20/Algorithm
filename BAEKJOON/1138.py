n = int(input())
lst = list(map(int, input().split()))
a = [0] * n

for i in range(1, n+1):
    tmp = lst[i - 1]
    cnt = 0
    for j in range(n):
        if cnt == tmp and a[j] == 0:
            a[j] = i
            break
        elif a[j] == 0:
            cnt += 1
print(*a)
