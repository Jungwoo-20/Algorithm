inp = input()
sum = 0
left = 0
for i in range(len(inp)):
    if inp[i] == '(':
        left +=1
    elif inp[i] == ')':
        left -= 1
        if inp[i-1] == '(':
            sum += left
        else:
            sum+=1
print(sum)