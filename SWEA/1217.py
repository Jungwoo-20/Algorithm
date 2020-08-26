T = 10

def solve(num, cnt):
    global a, b, result
    if cnt == b:
        result = num
        return result
    solve(num * a, cnt + 1)


for cnt in range(1, T + 1):
    count = int(input())
    a, b = list(map(int, input().split()))
    solve(a, 1)
    print('#' + str(count) + ' ' + str(result))