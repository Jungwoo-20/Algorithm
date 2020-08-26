T = int(input())
for cnt in range(1, T + 1):
    a, b, c = list(map(int, input().split()))
    result = 0
    if a == b:
        result = c
    elif a == c:
        result = b
    else:
        result = a
    print('#' + str(cnt) + ' ' + str(result))
