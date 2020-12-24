def pseudo(mun, left, right):
    while left < right:
        if mun[left] == mun[right]:
            left += 1
            right -= 1
        else:
            return 1
    return 0

def palindrome(mun, left, right):
    while left < right:
        if mun[left] == mun[right]:
            left += 1
            right -= 1
        else:
            tmp1 = pseudo(mun, left + 1, right)
            tmp2 = pseudo(mun, left, right - 1)
            if tmp1 == 0 or tmp2 == 0:
                return 1
            else:
                return 2
    return 0


n = int(input())
for i in range(n):
    mun = list(input())
    res = palindrome(mun, 0, len(mun) - 1)
    print(res)
