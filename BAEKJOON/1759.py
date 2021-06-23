import sys
from itertools import combinations

alpha = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, sys.stdin.readline().split())

password = sorted(list(map(str, sys.stdin.readline().split())))

password = combinations(password, L)
for i in password:
    cnt = 0
    for j in i:
        if j in alpha:
            cnt += 1
    if cnt >= 1 and cnt <= L - 2:
        print(''.join(i))
