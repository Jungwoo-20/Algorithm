def dfs(idx, max_sum):
    global num
    if max_sum >= num:
        return
    if idx >= n:
        if max_sum >= b:
            num = max_sum
        return
    visited[idx] = True
    dfs(idx + 1, max_sum + s[idx])
    visited[idx] = False
    dfs(idx + 1, max_sum)


for cnt in range(1, int(input()) + 1):
    n, b = list(map(int, input().split()))
    s = list(map(int, input().split()))
    num = 999999
    visited = [False] * n
    dfs(0, 0)
    print('#' + str(cnt) + ' ' + str(num-b))
