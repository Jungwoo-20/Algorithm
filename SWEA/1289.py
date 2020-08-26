T = int(input())
for cnt in range(1, T + 1):
    n = input()
    result = 0
    chk = '0'
    for i in range(len(n)):
        if n[i] != chk:
            result +=1
            chk = n[i]
    print('#' + str(cnt) + ' ' + str(result))