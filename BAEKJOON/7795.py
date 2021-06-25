import sys
import bisect

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = sorted(list(map(int, sys.stdin.readline().split())))
    B = sorted(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    for i in A:
        cnt += bisect.bisect(B, i - 1)
    print(cnt)
