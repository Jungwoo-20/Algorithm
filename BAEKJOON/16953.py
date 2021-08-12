import sys
from collections import deque

A, B = list(map(int, sys.stdin.readline().split()))


def bfs(queue):
    while queue:
        _x, cnt = queue.popleft()
        if _x == B:
            return cnt
        else:
            if _x * 2 <= B:
                queue.append((_x * 2, cnt + 1))
            if int(str(_x) + '1') <= B:
                queue.append((int(str(_x) + '1'), cnt + 1))
    return res


res = -1
q = deque()
q.append((A, 1))

print(bfs(q))
