def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            number = list(format(number, 'b'))
            number[-1] = '1'
        else:
            number = format(number, 'b')
            number = '0' + number
            idx = number.rfind('0')
            number = list(number)
            number[idx] = '1'
            number[idx + 1] = '0'
        res = int("".join(number), 2)
        answer.append(res)
    return (answer)

numbers = [2,7]
print(solution(numbers))
