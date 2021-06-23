import sys

N, K = map(int, sys.stdin.readline().split())
stk1 = [i for i in range(1, N + 1)]
stk2 = []
kill = 0
for i in range(N):
    kill += K - 1
    if kill >= len(stk1):
        kill %= len(stk1)
    stk2.append(str(stk1.pop(kill)))
print('<', ', '.join(stk2), '>', sep='')
