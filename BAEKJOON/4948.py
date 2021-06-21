N = 123456 * 2 + 1
flag = [True] * N
for i in range(2, int(N ** 0.5) + 1):
    if flag[i]:
        for j in range(2 * i, N, i):
            flag[j] = False


def chk(val):
    cnt = 0
    for i in range(val + 1, val * 2 + 1):
        if flag[i]:
            cnt += 1
    print(cnt)


while True:
    n = int(input())
    if n == 0:
        break
    chk(n)
