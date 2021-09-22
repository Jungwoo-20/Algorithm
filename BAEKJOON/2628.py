import sys

width, height = map(int, sys.stdin.readline().split())
num = int(sys.stdin.readline())
x = [0, width]
y = [0, height]
for _ in range(num):
    flag, cm = map(int, sys.stdin.readline().split())
    if flag == 0:
        y.append(cm)
    else:
        x.append(cm)
res = 0
x.sort()
y.sort()
for i in range(1, len(x)):
    for j in range(1, len(y)):
        a = x[i] - x[i - 1]
        b = y[j] - y[j - 1]
        res = max(res, a * b)
print(res)