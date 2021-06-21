def solution(num):
    num = list(map(str, num))
    num.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(num)))


num = [6, 10, 2]
print(solution(num))
