def solution(s):
    answer = s.split(' ')
    for i in range(len(answer)):
        _split = list(answer[i])

        for j in range(len(_split)):
            if j % 2 == 0:
                _split[j] = _split[j].upper()
            else:
                _split[j] = _split[j].lower()
        answer[i] = ''.join(_split)
    result = ' '.join(answer)
    return result


solution("try hello world")
