import sys

N = bin(int(sys.stdin.readline()))[2:]
res = 0
for i in range(len(N)):
    tmp = int(N[i])
    if tmp == 1:
        res += 3 ** (len(N) - i - 1)
print(res)
