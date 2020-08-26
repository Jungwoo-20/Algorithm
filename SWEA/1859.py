case = int(input())

for tmp in range(1, case + 1):
    N = int(input())

    a = []
    b = []
    b = input().split()

    for i in range(0, N):
        a.append(int(b[i]))

    result = 0
    max_num = 0
    for j in range(N-1, -1,-1):
        if max_num > a[j]:
            result += max_num - a[j]
        else:
            max_num = a[j]

    print("#" + str(tmp) + " " + str(result))