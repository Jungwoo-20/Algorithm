import sys
from collections import Counter
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
#산술평균
print(round(sum(num)/len(num)))
num.sort()
#중앙
print(num[(n//2)])
mode_dict = Counter(num)
num1 = mode_dict.most_common()
print(num1)
if len(num) > 1:
    if num1[0][1] == num1[1][1]:
        print(num1[1][0])
    else:
        print(num1[0][0])
else:
    print(num1[0][0])
print(num[-1]-num[0])