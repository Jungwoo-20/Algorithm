import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
res = permutations(range(1, N + 1), M)
for i in res:
    print(' '.join(map(str, i)))
