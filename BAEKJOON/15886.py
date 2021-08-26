import sys

N = int(sys.stdin.readline())
matrix = sys.stdin.readline().rstrip()
cnt = 0
for i in range(len(matrix) - 1):
    if matrix[i] == 'E' and matrix[i+1] == 'W':
        cnt+=1
print(cnt)