# 위, 아래, 오, 왼
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(dirs):
    answer = 0
    direction = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
    dirs = list(dirs)
    visited = set()
    x, y = 0, 0
    for i in dirs:
        idx = direction[i]
        _x = x + dx[idx]
        _y = y + dy[idx]
        if _x < -5 or _x > 5 or _y < -5 or _y > 5:
            continue
        if (x, y, _x, _y) not in visited:
            visited.add((x, y, _x, _y))
            visited.add((_x, _y, x, y))
            answer += 1
        x = _x
        y = _y
    return answer


dirs = "ULURRDLLU"
print(solution(dirs))
