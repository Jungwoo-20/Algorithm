import sys

n = int(sys.stdin.readline())
mun = [sys.stdin.readline().strip() for _ in range(n)]
mun = list(set(mun))
mun.sort(key=lambda x: (len(x), x))
for i in mun:
    print(i)
