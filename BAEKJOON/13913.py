import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

# 시간 계산
queue = deque()
queue.append(N)
visited = [[-1, -1] for _ in range(100002)]  # [방문 회수, 이전의 위치]
visited[N][0] = 0

# 경로 탐색
dist = deque()
dist.append(K)


def bfs(q):
    while q:
        x = q.popleft()
        if x == K:
            return visited[x][0]
        for _x in [x + 1, x - 1, x * 2]:
            if 0 <= _x < 100001:
                if visited[_x][0] == -1:
                    visited[_x][0] = visited[x][0] + 1
                    visited[_x][1] = x
                    q.append(_x)


def distCheck(dist):
    global K
    while True:
        if visited[K][1] != -1:
            dist.appendleft(visited[K][1])
            K = visited[K][1]
        else:
            break



print(bfs(queue))
distCheck(dist)
print(' '.join(map(str, dist)))
