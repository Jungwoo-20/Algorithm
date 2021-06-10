import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lst = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)


def bfs(start):
    queue = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1
    while queue:
        cnt = queue.popleft()
        for i in lst[cnt]:
            if visited[i] == 0:
                visited[i] = visited[cnt] + 1
                queue.append(i)
    return visited


res = bfs(1)
print(res.count(2) + res.count(3))
