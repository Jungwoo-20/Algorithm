N = int(input())
start = dict()
end = []
cnt = 0
for i in range(N):
    start[input()] = i
for _ in range(N):
    end.append(input().rstrip())
for i in range(N - 1):
    for j in range(i + 1, N):
        if start[end[i]] > start[end[j]]:
            cnt += 1
            break
print(cnt)
