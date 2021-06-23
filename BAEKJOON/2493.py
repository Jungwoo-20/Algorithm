import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
stk = []
res = []

for i in range(N):
    while stk:
        if stk[-1][1] > lst[i]:
            res.append(stk[-1][0] + 1)
            break
        else:
            stk.pop()
    if not stk:
        res.append(0)
    stk.append([i, lst[i]])
print(*res)
