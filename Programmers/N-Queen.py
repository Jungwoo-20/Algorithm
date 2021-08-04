def dfs(queen, n, row):
    cnt = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for x in range(row):
            if queen[x] == queen[row]:
                break
            if abs(queen[row] - queen[x]) == row - x:
                break
        else:
            cnt += dfs(queen, n, row + 1)
    return cnt


def solution(n):
    queen = [0] * n
    return dfs(queen, n, 0)


print(solution(4))
