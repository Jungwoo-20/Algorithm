import sys


def solution(n):
    cnt = 0
    num = 1
    while True:
        flag = True
        _num = str(num)
        if len(_num) == 1: # 9까지는 감소하는
            pass
        else:
            for i in range(1, len(_num)):
                if int(_num[i - 1]) > int(_num[i]):
                    continue
                else: # 수가 감소하지 않는 경우
                    start = _num[:i - 1] # 앞자리와
                    mid = str(int(_num[i - 1]) + 1) # 현재위치의 +1
                    end = '0' + _num[i + 1:] # mid의 시작인 0인 수 부터
                    num = int(start + mid + end) #str로 합산하여 새로운 num부터 체크(시간 초과 해결 방법)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:
                return num
            num += 1


N = int(sys.stdin.readline())
if N == 0:
    print(0)
elif N >= 1023:
    print(-1)
else:
    print(solution(N))
