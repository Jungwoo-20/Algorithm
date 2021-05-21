import sys
import itertools

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

arr = [sys.stdin.readline().rstrip() for _ in range(N)]

result = set()
for i in itertools.permutations(arr, K):
    result.add(''.join(i))
print(len(result))
