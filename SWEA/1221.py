T = int(input())
for cnt in range(1, T + 1):
    n = input()
    num = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    arr = input().split()
    result = ''
    for i in arr:
        num[i] += 1
    for k, v in num.items():
        tmp = ' '.join([k] * v)
        result += tmp + ' '
    print('#' + str(cnt))
    print(result[:len(result)-1])
