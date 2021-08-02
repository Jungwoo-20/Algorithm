def solution(price, money, count):
    total=0
    for i in range(1,count+1):
        total+= (i*price)
    if money-total>0:
        return 0
    else:
        return abs(money-total)