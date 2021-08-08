def make_tree(lst, start):
    mid = len(lst) // 2
    tree[start].append(lst[mid])
    if len(lst) == 1:
        return
    make_tree(lst[:mid], start + 1)
    make_tree(lst[mid + 1:], start + 1)


K = int(input())
lst = list(map(int, input().split()))
tree = [[] for i in range(K)]  # 완성된 트리

make_tree(lst, 0)
for i in range(K):
    print(*tree[i])
