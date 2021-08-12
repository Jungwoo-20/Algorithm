import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

q = deque()
q.append(N)
visited = [-1] * 100001

visited[N] = 0
while q:
    x = q.popleft()
    if x == K:
        print(visited[K])
        sys.exit()
    for _x in [x + 1, x - 1]:
        if 0 <= _x < 100001:
            if visited[_x] == -1 or visited[_x] >= visited[x] + 1:
                visited[_x] = visited[x] + 1
                q.append(_x)
    for _x in [x * 2]:
        if 0 <= _x < 100001:
            if visited[_x] == -1 or visited[_x] >= visited[x]:
                visited[_x] = visited[x]
                q.append(_x)
