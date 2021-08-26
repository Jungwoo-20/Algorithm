import sys
n = int(sys.stdin.readline())
res = {}
for _ in range(n):
    name, flag = map(str, sys.stdin.readline().split())
    if flag == 'enter':
        res[name] = 'enter'
    else:
        if res[name]:
            del res[name]

for i in sorted(res, reverse=True):
    print(i)