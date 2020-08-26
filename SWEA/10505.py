T = int(input())
for cnt in range(1, T + 1):
    people = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)/people
    count = 0
    for i in arr:
        if i<=total:
            count+=1
    print('#' + str(cnt) + ' ' + str(count))