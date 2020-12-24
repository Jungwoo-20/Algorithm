import sys

input=sys.stdin.readline

lis = []

inputnum = int(input())

for i in range(inputnum):
    num = int(input())
    if num == 0:
        del lis[-1]
    else:
        lis.append(num)
if not lis:
    print(0)
else:
    print(sum(lis))