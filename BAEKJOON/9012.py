a = int(input())
for i in range(a):
    data = input()
    datalist = list(data)
    sum = 0
    for j in datalist:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")