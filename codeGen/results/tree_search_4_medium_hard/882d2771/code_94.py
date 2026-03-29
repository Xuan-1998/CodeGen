MOD = 10**9 + 7

def f(r, k):
    if (r, k) in memo:
        return memo[(r, k)]
    
    if r == 0 or k == 0:
        res = r if k == 0 else 0
    else:
        res = float('inf')
        for i in range(l, r+1):
            res = min(res, f(i-1, k-1) + 1)
    
    memo[(r, k)] = res % MOD
    return res

memo = {}
t, l, r = map(int, input().split())
print(f(r, t))
