import sys

S = list(sys.stdin.readline().rstrip())
K = sys.stdin.readline().rstrip()
tmp = []
for i in S:
    if not i.isdigit():
        tmp.append(i)
    else:
        continue
tmp = ''.join(tmp)
if K in tmp:
    print(1)
else:
    print(0)
