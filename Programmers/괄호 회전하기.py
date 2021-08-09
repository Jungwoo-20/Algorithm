def solution(s):
    s = list(s)
    stk = []
    cnt = 0
    for i in range(len(s)):
        flag = True
        if i != 0:
            s.append(s.pop(0))
        for j in s:
            try:
                if j == '(' or j == '[' or j == '{':
                    stk.append(j)
                elif j == '}' and stk[-1] == '{':
                    stk.pop()
                elif j == ']' and stk[-1] == '[':
                    stk.pop()
                elif j == ')' and stk[-1] == '(':
                    stk.pop()
            except:
                flag = False
                break
        if not stk and flag:
            cnt+=1
    return cnt
