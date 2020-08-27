for t in range(int(input())):
    N = int(input())
    card = list(map(str, input().split()))
    print(f"#{t+1}",end=' ')
    if len(card) % 2 == 0:
        for i in range(N//2):
            print(f"{card[i]} {card[N//2+i]}",end=" ")
        print()
    else:
        for i in range(N//2):
            print(f"{card[i]} {card[N//2+i+1]}",end=" ")
        print(f"{card[N//2]}",end=" ")
        print()
