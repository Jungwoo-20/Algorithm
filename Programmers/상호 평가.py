import numpy as np

def check_flag(ans):
    if ans >= 90:
        return 'A'
    elif ans >= 80:
        return 'B'
    elif ans >= 70:
        return 'C'
    elif ans >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    result = ''
    for i in range(len(scores)):
        res = []
        for j in range(len(scores)):
            res.append(scores[j][i])
        me = res[i]
        if me == max(res) or me == min(res):
            pos = np.where(np.array(res) == me)[0]
            if len(pos) == 1:
                res.remove(me)
        answer = sum(res) / len(res)
        result += check_flag(answer)
    return result


score = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]
print(solution(score))
