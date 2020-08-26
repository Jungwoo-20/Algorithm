T = 10
for case in range(1, T + 1):
    n = int(input())
    string = input()
    arr = input()
    cnt = arr.count(string)
    print('#' + str(n) + ' ' + str(cnt))