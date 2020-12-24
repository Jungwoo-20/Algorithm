ans = 0

cnt = 0
while True:
    stack = []
    ans = 0
    n = input()
    for i in n:
        if i == '{':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                ans += 1
                stack.append('{')
        if i == '-':
            exit()
    if stack:
        ans += len(stack) // 2
    cnt += 1
    print(str(cnt) + '. ' + str(ans))
