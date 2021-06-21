n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
res = []
for i in range(n):
    idx = b.index(a[i])
    res.append(idx)
    b[idx] = -1
print(*res)
