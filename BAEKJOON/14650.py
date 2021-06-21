import sys

sys.setrecursionlimit(1000000)

N = int(input())
res = 0


def num(n, sum):
    global res
    for i in range(3):
        if n == 0 and i == 0:
            continue
        if n == N:
            if sum % 3 == 0:
                res += 1
                return res
        else:
            num(n + 1, int(str(sum + i)))


num(0, 0)
print(res)
