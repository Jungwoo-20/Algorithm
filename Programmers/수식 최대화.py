from itertools import permutations


def calculate(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def solve(expression, op):
    num = []
    tmp = ''
    for i in expression:
        if i.isdigit():
            tmp += i
        else:
            num.append(tmp)
            num.append(i)
            tmp = ''
    num.append(tmp)
    for i in op:
        stk = []
        while num:
            tmp = num.pop(0)
            if tmp == i:
                stk.append(calculate(stk.pop(), num.pop(0), i))
            else:
                stk.append(tmp)
        num = stk
    return abs(int(num[0]))


def solution(expression):
    op = ['+', '-', '*']
    op = list(set(permutations(op, len(op))))
    res = []
    for i in op:
        res.append(solve(expression, i))
    return max(res)


expression = "100-200*300-500+20"
print(solution(expression))
