import sys

n = int(sys.stdin.readline())
matrix = list(map(int, sys.stdin.readline().split()))
student = int(sys.stdin.readline())
on_off = {0: 1, 1: 0}
for i in range(student):
    se, num = map(int, sys.stdin.readline().split())  # se 1:남, 2:여
    if se == 1:
        tmp = num
        while num - 1 < n:
            matrix[num - 1] = on_off[matrix[num - 1]]
            num += tmp
    else:
        left = num - 2
        right = num
        matrix[num - 1] = on_off[matrix[num - 1]]
        while left >= 0 and right < n:
            if matrix[left] == matrix[right]:
                matrix[left] = on_off[matrix[left]]
                matrix[right] = on_off[matrix[right]]
            else:
                break
            left -= 1
            right += 1
for i in range(0, n, 20):
    print(*matrix[i:i + 20])
