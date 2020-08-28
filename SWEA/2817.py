def solve(i, sum):
    global cnt
    if i >= n:
        return
    temp = sum + arr[i]
    if temp == k:
        cnt += 1
    solve(i + 1, sum)
    solve(i + 1, temp)


T = int(input())
for cnt1 in range(1, T + 1):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    cnt = 0
    solve(0, 0)
    print('#' + str(cnt1) + ' ' + str(cnt))
