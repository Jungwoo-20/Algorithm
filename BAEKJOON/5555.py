def find_key(mun, key, key_len):
    for i in range(10):
        for j in range(key_len):
            nj = i + j
            if nj >= 10:
                nj -= 10
            if mun[nj] != key[j]:
                break
        else:
            return True
    return False


key = input()
key_len = len(key)
res = 0
for _ in range(int(input())):
    if find_key(input(), key, key_len):
        res += 1
print(res)
