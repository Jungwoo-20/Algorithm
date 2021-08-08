def solution(arr, N):
    if N == 1:
        return arr[0][0]
    _arr = [[] for _ in range(N // 2)]
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            _arr[i // 2].append(sorted(arr[i][j], arr[i + 1][j], arr[i][j + 1], arr[i + 1][j + 1])[2])
    return solution(_arr,N//2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(solution(arr, N))
