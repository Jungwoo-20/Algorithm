T = int(input())
for cnt in range(1, T + 1):
    N = list(input())
    H = input()
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in arr:
        N.insert(i,'-')
    print('#' + str(cnt), end=' ')
    for i in N:
        print(i, end='')
    print()