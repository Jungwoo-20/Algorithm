n = input()
tmp = input()
gil = len(tmp)
last = tmp[-1]
stack = []

for i in n:
    stack.append(i)
    if i == last and ''.join(stack[-gil:]) == tmp:
        del stack[-gil:]

result = ''.join(stack)

if result != '':
    print(result)
else:
    print("FRULA")