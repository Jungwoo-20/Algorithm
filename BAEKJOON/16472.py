import sys

N = int(sys.stdin.readline())
str = sys.stdin.readline().rstrip()
start, res = 0, 0
dict = {}
for rear in range(len(str)):
    dict.setdefault(str[rear], 0)
    dict[str[rear]] += 1
    while len(dict) > N:
        dict[str[start]] -= 1
        if dict[str[start]] == 0:
            del dict[str[start]]
        start += 1
    res = max(res, rear - start + 1)
print(res)
