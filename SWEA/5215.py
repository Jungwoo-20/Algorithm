def dfs(idx, sum_result, sum_kal):
    global max_result
    if sum_kal > l:
        return
    if max_result < sum_result:
        max_result = sum_result
    if idx == n:
        return
    score, cal = arr[idx]
    dfs(idx + 1, sum_result + score, sum_kal + cal)
    dfs(idx + 1, sum_result, sum_kal)


for cnt in range(1, int(input()) + 1):
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_result = 0
    dfs(0,0,0)
    print('#' + str(cnt) + ' ' + str(max_result))
