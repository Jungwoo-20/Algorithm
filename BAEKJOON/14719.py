import sys

H, W = list(map(int, sys.stdin.readline().split()))
height = list(map(int, sys.stdin.readline().split()))

maxHeight = 0
res = 0

for i in range(len(height)):
    minValue = min(max(height[i:]), max(height[:i+1]))
    res += abs(height[i]-minValue)
print(res)