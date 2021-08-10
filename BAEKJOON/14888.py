from itertools import permutations
import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
operation = ['+', '-', '*', '/']
operNum = list(map(int, sys.stdin.readline().split()))
op = []
for i in range(4):
    for j in range(operNum[i]):
        op.append(operation[i])
op = list(set(permutations(op, len((op)))))

res = []
for i in op:
    tmp = num[0]
    for j in range(len(num) - 1):
        if i[j] == '+':
            tmp += num[j + 1]
        elif i[j] == '-':
            tmp -= num[j + 1]
        elif i[j] == '*':
            tmp *= num[j + 1]
        else:
            if tmp // num[j + 1] < 0:
                tmp = -(-tmp // num[j + 1])
            else:
                tmp = tmp // num[j + 1]
    res.append(tmp)

print(max(res))
print(min(res))
