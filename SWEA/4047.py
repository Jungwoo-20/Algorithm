T = int(input())
for cnt in range(1, T + 1):
    S = input()
    S_list = []
    card = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    print('#' + str(cnt), end=' ')
    for i in range(0, len(S), 3):
        S_list.append(S[i:i + 3])
    if len(set(S_list)) != len(S_list):
        print('ERROR')
    else:
        for i in S_list:
            card[i[0]] -=1
        print(*card.values())

