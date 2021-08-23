def solution(table, languages, preference):
    score = {}
    answer = ''
    res = 0
    for i, j in zip(languages, preference):
        score[i] = j
    for i in table:
        tmp = i.split(' ')
        tmp_score = 0
        cnt = 0
        for j in range(len(tmp)-1, -1, -1):
            tmp_score += 1
            try:
                if score[tmp[j]]:
                    cnt += tmp_score * score[tmp[j]]
            except:
                pass
        if cnt > res:
            answer = tmp[0]
            res = cnt
        elif cnt == res:
            if answer < tmp[0]:
                continue
            else:
                answer = tmp[0]

    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

print(solution(table, languages, preference))
