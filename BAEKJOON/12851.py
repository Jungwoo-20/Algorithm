import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

q = deque()
q.append(N)
visited = [-1] * 100001

visited[N] = 0
cnt = 0
while q:
    x = q.popleft()
    if x == K:
        cnt += 1
    for _x in [x + 1, x - 1, x * 2]:
        if 0 <= _x < 100001:
            if visited[_x] == -1 or visited[_x] >= visited[x] + 1:
                visited[_x] = visited[x] + 1
                q.append(_x)
print(visited[K])
print(cnt)
