import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
home = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
visited[X] = 0
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    home[A].append(B)

queue = deque([X])
while queue:
    tmp = queue.popleft()
    for i in home[tmp]:
        if visited[i] == -1:
            visited[i] = visited[tmp] + 1
            queue.append(i)
for i in range(N + 1):
    if visited[i] == K:
        print(i)
if K not in visited:
    print(-1)
