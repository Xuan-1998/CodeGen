def min_F(n, s, a):
    if n == 0:
        return a
    elif (n, s, a) in cache:
        return cache[(n, s, a)]
    
    res = float('inf')
    for x in range(1, a+1):
        y = a - x
        if (x - s) * (y - s) >= 0:
            F = min_F(n-1, s, x) + x*y
            res = min(res, F)
    
    cache[(n, s, a)] = res
    return res

cache = {}

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_F(n, s, a[-1]))
