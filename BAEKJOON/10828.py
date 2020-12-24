import sys

input=sys.stdin.readline

lis = []
def push(a):
    lis.append(a)
def pop():
    try:
        print(lis.pop())
    except:
        print("-1")
def size():
    print(len(lis))

def empty():
    if len(lis) >0:
        print("0")
    else:
        print("1")

def top():
    try:
        print(lis[-1])
    except:
        print("-1")

inputnum = int(input())

for i in range(inputnum):
    data = input().split()
    if data[0] == "push":
        push(data[1])
    elif data[0] == "pop":
        pop()
    elif data[0] == "size":
        size()
    elif data[0] == "empty":
        empty()
    elif data[0] == "top":
        top()