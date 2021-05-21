import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
start, end = 0, N - 1
_result = sys.maxsize
while start < end:
    tmp = arr[start] + arr[end]
    if abs(tmp) < _result:
        left = start
        right = end
        _result = abs(tmp)
    if tmp < 0:
        start += 1
    elif tmp > 0:
        end -= 1
    else:
        break
print(str(arr[left]) + ' ' + str(arr[right]))
