from itertools import permutations


def flag(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    _tmp = []
    for i in range(1, len(numbers) + 1):
        tmp = list(map(''.join, permutations(list(numbers), i)))
        for j in list(set(tmp)):
            if flag(int(j)):
                _tmp.append(int(j))
    return len(set(_tmp))


print(solution('011'))
