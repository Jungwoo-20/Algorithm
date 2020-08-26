T = int(input())
arr = ['a','e','i','o','u']
for cnt in range(1, T + 1):
    n = list(map(str, input()))
    temp = []
    result = ''
    for i in n:
        if i not in arr:
            temp.append(i)

    for i in temp:
        result +=i
    print('#' + str(cnt) + ' ' + str(result))