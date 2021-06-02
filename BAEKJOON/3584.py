import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    parent = [0 for _ in range(N + 1)]
    for i in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())
        parent[B] = A
    a, b = map(int, sys.stdin.readline().split())
    parentA = [a]
    parentB = [b]
    while parent[a]:
        parentA.append(parent[a])
        a = parent[a]
    while parent[b]:
        parentB.append(parent[b])
        b = parent[b]

    levelA = len(parentA) - 1
    levelB = len(parentB) - 1
    while parentA[levelA] == parentB[levelB]:
        levelA -= 1
        levelB -= 1
    print(parentA[levelA + 1])
