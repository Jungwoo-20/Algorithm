import sys

n, s = map(int, sys.stdin.readline().split())
matrix = list(map(int, sys.stdin.readline().split()))
start = 0
end = 1
ans = 100000001
tmp = [0] * (n + 1)
for i in range(1, n + 1):
    tmp[i] = tmp[i - 1] + matrix[i - 1]
print(tmp)
while start != n:
    if tmp[end] - tmp[start] >= s:
        if end - start < ans:
            ans = end - start
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1
if ans == 100000001:
    print(0)
else:
    print(ans)
