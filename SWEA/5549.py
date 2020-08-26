T = int(input())
for cnt in range(1, T + 1):
    tc = list(input())
    result = ''
    if int(tc[-1])%2 == 0:
        result = 'Even'
    else:
        result = 'Odd'
    print('#' + str(cnt) + ' ' + str(result))