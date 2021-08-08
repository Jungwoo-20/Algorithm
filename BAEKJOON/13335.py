n, w, l = list(map(int, input().split()))
lst = list(map(int, input().split()))
bridge = [0] * w
time = 0
while lst:
    time += 1
    bridge.pop(0)
    if lst:
        if lst[0] + sum(bridge) <= l:
            bridge.append(lst.pop(0))
        else:
            bridge.append(0)
print(time + len(bridge))
