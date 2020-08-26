T = int(input())

for cnt in range(1, T + 1):
    L, U, X = list(map(int, input().split()))
    result = 0
    if X > U:
        result = -1
    elif X < L:
        result = L - X
    print('#' + str(cnt) + ' ' + str(result))
