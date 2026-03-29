def beauty_sum(t, l, r):
    MOD = 10**9 + 7

    def f(n):
        if n == 2:
            return min(1, 1)
        if memoized[n] > 0:
            return memoized[n]
        
        res = float('inf')
        for i in range(1, n//2 + 1):
            res = min(res, f(i) + f(n-i))
        memoized[n] = res
        return res

    memoized = [0]*(r+1)
    res = sum(t*f(l+i-1) - l*f(r) for i in range(1, t+1)) % MOD
    return res


import sys
t, l, r = map(int, sys.stdin.readline().split())
print(beauty_sum(t, l, r))
