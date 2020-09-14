for cnt in range(1, int(input()) + 1):
    n = input()
    flag = 'Exist'
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            if n[i] == '?' or n[-1-i] == '?':
                continue
            else:
                flag = 'Not exist'
    print('#' + str(cnt) + ' ' + str(flag))