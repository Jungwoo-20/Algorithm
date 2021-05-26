import sys

g, s = map(int, sys.stdin.readline().split())
left, right, cnt = 0, 0, 0
W = sys.stdin.readline().rstrip()
S = sys.stdin.readline().rstrip()
arr1 = [0] * 52
arr2 = [0] * 52

for i in range(g):
    if 'a' <= W[i] <= 'z':
        arr1[ord(W[i]) - ord('a')] += 1
    else:
        arr1[ord(W[i]) - ord('A') + 26] += 1

for i in range(s):
    if 'a' <= S[i] <= 'z':
        arr2[ord(S[i]) - ord('a')] += 1
    else:
        arr2[ord(S[i]) - ord('A') + 26] += 1
    right += 1
    if right == g:
        if arr1 == arr2:
            cnt += 1
        if 'a' <= S[left] <= 'z':
            arr2[ord(S[left]) - ord('a')] -= 1
        else:
            arr2[ord(S[left]) - ord('A') + 26] -= 1
        left += 1
        right -= 1
print(cnt)
