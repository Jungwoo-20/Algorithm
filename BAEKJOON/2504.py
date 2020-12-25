tmp = 1
res = 0
flag = False
n = input()
stack = []
for i in n:
    if i == '(':
        stack.append('(')
        tmp *= 2
    elif i == '[':
        stack.append('[')
        tmp *= 3
    elif i == ')':
        if stack.count() == 0:
            flag = True
            break
        if stack[-1] == '(':
            if (stack[i - 1] == '('):
                res += tmp
            stack.pop()
            tmp /= 2
        else:
            flag = True
            break
    elif stack[i] == ']':
        if stack.count() == 0:
            flag = True
            break
        if stack[-1] == '[':
            if stack[i - 1] == '[':
                res += tmp
            stack.pop()
            tmp /= 3
        else:
            flag = True
            break
    if flag == True or stack.count() == 0:
        print(0)
    else:
        print(res)
