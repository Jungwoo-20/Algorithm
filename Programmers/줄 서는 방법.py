from itertools import permutations


def solution(n, k):
    answer = [i for i in range(1, n + 1)]
    answer = list(permutations(answer, 3))
    answer.sort()
    return list(answer[k-1])


n = 3
k = 5
print(solution(n, k))
