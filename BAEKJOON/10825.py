import sys

n = int(sys.stdin.readline())
student = []
for _ in range(n):
    name, kor, math, eng = list(map(str, input().split()))
    student.append([name, int(kor), int(math), int(eng)])

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in student:
    print(i[0])
