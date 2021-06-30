from collections import deque


def bfs(visited, lst):
    queue = deque()
    queue.append(1)
    visited[1] = 1
    while queue:
        tmp = queue.popleft()
        for i in lst[tmp]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[tmp] + 1


def solution(n, edge):
    answer = 0
    visited = [0] * (n + 1)
    lst = [[] for _ in range(n + 1)]
    for i in edge:
        start, end = i[0], i[1]
        lst[start].append(end)
        lst[end].append(start)
    bfs(visited, lst)
    score = max(visited)
    for i in visited:
        if i == score:
            answer+=1
    return answer
