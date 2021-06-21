def solution(numbers, target):
    arr = [0]  # 초기 값
    for i in numbers:
        tmp = []
        for j in arr:
            tmp.append(j + i)
            tmp.append(j - i)
        arr = tmp
    return arr.count(target)


num = [1, 1, 1, 1, 1]
print(solution(num,3))
