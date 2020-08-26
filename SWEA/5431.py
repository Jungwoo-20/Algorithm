T = int(input())
for cnt in range(1, T + 1):
    total, suc = list(map(int, input().split()))
    result = []
    for i in range(1, total + 1):
        result.append(i)
    arr = list(map(int, input().split()))
    set_result = set(result)
    set_arr = set(arr)
    temp = set_result - set_arr
    print('#' + str(cnt), end=' ')
    for i in temp:
        print(i, end=' ')
    print()