T = int(input())
for cnt in range(1, T + 1):
    result = 0
    a = []
    b = []
    n = list(input())
    m = n[:]
    while n:
        a.append(n.pop())
        b.append(m.pop(0))
    if a == b:
        result = 1
    print('#' + str(cnt) + ' ' + str(result))