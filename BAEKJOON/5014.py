import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())


def bfs():
    queue = deque([S])
    visit = [0] * (F + 1)
    visit[S] = 1
    while queue:
        cnt = queue.popleft()
        if cnt == G:
            return print(visit[G] - 1)
        else:
            u = cnt + U
            d = cnt - D
            if u <= F and visit[u] == 0:
                queue.append(u)
                visit[u] = visit[cnt] + 1  # cnt count
            if d > 0 and visit[d] == 0:
                queue.append(d)
                visit[d] = visit[cnt] + 1
    else:
        return print('use the stairs')


bfs()
