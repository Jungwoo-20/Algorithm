def prime(n):
    a = [False, False] + [True] * (n - 1) 
    for k in range(2, int(n ** 0.5 + 1.5)):
        if a[k]:
            a[k*2::k] = [False] * ((n - k) // k) 
    return [x for x in range(n+1) if a[x]]
print(' '.join(map(str, prime(1000000))))