import sys
from collections import deque

S = int(sys.stdin.readline())
q = deque()
q.append((1, 0))
visited = dict()
visited[(1, 0)] = 0  # 현재 개수, 클립보드 이모티콘 개수


def emoticon(q):
    while q:
        s, c = q.popleft()
        if s == S:
            return visited[(s, c)]
        if (s, s) not in visited.keys():  # 화면 이모티콘 복사
            visited[(s, s)] = visited[(s, c)] + 1
            q.append((s, s))
        if (s + c, c) not in visited.keys():  # 클립보드에 있는 이모티콘을 붙여넣기
            visited[(s + c, c)] = visited[(s, c)] + 1
            q.append((s + c, c))
        if (s - 1, c) not in visited.keys():  # 이모티콘 하나 삭제
            visited[(s - 1, c)] = visited[(s, c)] + 1
            q.append((s - 1, c))


print(emoticon(q))
