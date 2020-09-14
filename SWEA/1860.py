for cnt in range(1, int(input()) + 1):
    N, M, K = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if sorted(a)[i]//M*K<i+1:
            result = 'Impossible'
            break
        else:
            result = 'Possible'
    print('#' + str(cnt) + ' ' + str(result))