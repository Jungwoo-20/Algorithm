import sys


# 추가 변수형 처리
def solution(str):
    for i in range(len(str) - 2, -1, -1):
        if str[i] in '&*':
            print(str[i], end='')
        elif str[i] == ']':
            print('[]', end='')
        elif str[i] == '[':
            continue
        else:
            print(' ', end='')
            for j in range(i + 1):
                print(str[j], end='')
            return


datatype, *value = sys.stdin.readline().split()
for i in value:
    print(datatype, end='')
    solution(i)
    print(';')
