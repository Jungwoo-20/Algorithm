import sys

left = list(sys.stdin.readline().rstrip())
right = []

M = int(sys.stdin.readline())
for i in range(M):
    tmp = sys.stdin.readline().strip()
    if tmp[0] == 'P':
        left.append(tmp[2])
    elif tmp[0] == 'L':
        if left:
            right.append(left.pop())
    elif tmp[0] == 'D':
        if right:
            left.append(right.pop())
    else:
        if left:
            left.pop()
left.extend(right[::-1])
print(''.join(left))
