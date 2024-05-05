mod = 10**9 + 7
t, l, r = map(int, input().split())

def f(i):
    if i < 0:
        return 0
    if memo[i] != -1:
        return memo[i]
    
    if i == 0:
        return 1
    
    res = float('inf')
    for j in range(l, r+1):
        res = min(res, f(j-1) + 1)
    memo[i] = res
    return res

memo = [-1]*(r+1)

for i in range(r, l-1, -1):
    res = 0
    for j in range(l, r+1):
        if j <= i:
            res += t*min(i-j+1, f(j)) % mod
    print((res-l*f(r)) % mod)
