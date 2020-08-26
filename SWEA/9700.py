T = int(input())
for cnt in range(1, T + 1):
    p, q = list(map(float, input().split()))
    s1 = (1-p)*q
    s2 = p*(1-q)*q
    result = ''
    if s1<s2:
        result = 'YES'
    else:
        result = 'NO'
    print('#' + str(cnt) + ' ' + str(result))