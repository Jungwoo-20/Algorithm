import sys
N, k,i = map(int,sys.stdin.readline().split())
cnt = 0
while k!= i:
    k -= k//2
    i -= i//2
    cnt+=1

print(cnt)