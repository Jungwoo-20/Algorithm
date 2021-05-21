import sys

N, M = map(int, sys.stdin.readline().split())
arr1 = []
for i in range(N):
    arr1.append(sys.stdin.readline().rstrip())
arr2 = []
for i in range(M):
    arr2.append(sys.stdin.readline().rstrip())

res = list(set(arr1) & set(arr2))
print(len(res))
for i in sorted(res):
    print(i)
