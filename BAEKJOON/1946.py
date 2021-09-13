import sys

t = int(sys.stdin.readline())
for _ in range(t):
    score = []
    cnt = 0
    n = int(sys.stdin.readline())
    for _ in range(n):
        paper, interview = map(int, sys.stdin.readline().split())
        score.append([paper, interview])
    score.sort()
    res = score[0][1]
    cnt+=1
    for i in range(1, len(score)):
        if res > score[i][1]:
            cnt+=1
            res = score[i][1]
    print(cnt)