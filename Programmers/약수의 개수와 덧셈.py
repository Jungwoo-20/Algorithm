def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        tmp = []
        for j in range(1, i+1):
            if i%j==0:
                if j in tmp or i%j in tmp:
                    continue
                if i//j == j:
                    tmp.append(j)
                else:
                    tmp.append(i//j)
                    tmp.append(j)
        if len(tmp)%2 ==0:
            answer+=i
        else:
            answer-=i
    return answer