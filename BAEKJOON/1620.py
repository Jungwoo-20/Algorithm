import sys

N, M = map(int, sys.stdin.readline().split())
# dictionary 탐색 시간 복잡도 O(1)
# list 탐색 시간 복잡도 O(n)
dic1 = {}
dic2 = {}
for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    dic1[i] = tmp
    dic2[tmp] = i
for i in range(M):
    key = sys.stdin.readline().rstrip()
    if key.isdigit():
        print(dic1[int(key) - 1])
    else:
        print(dic2[key] + 1)
