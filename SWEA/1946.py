T = int(input())
arr = []
for cnt in range(1, T + 1):
    num = int(input())
    result = ''
    for i in range(num):
        N, M = input().split()
        M = int(M)
        result += (N * M)
    print('#' + str(cnt))
    for i in range(len(result) // 10 + 1):
        print(result[i * 10: (i + 1) * 10])