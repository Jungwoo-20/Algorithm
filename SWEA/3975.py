result = []
for cnt in range(1, int(input()) + 1):
    a, b, c, d = list(map(int, input().split()))
    alice = a / b
    bob = c / d
    if alice>bob:
        result.append('ALICE')
    elif alice<bob:
        result.append('BOB')
    else:
        result.append('DRAW')
cnt = 1
for i in result:
    print('#' + str(cnt) + ' ' + i)
    cnt+=1
