import sys
sys.setrecursionlimit(2000)
mod = 10**9 + 7

def f(n):
    if n == 1:
        return 0
    memo = {}
    def rec(n, memo):
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            left = rec(n // 2, memo)
            right = rec(n // 2, memo)
            res = min(left + 1, right + 1)
        else:
            res = 1
        memo[n] = res
        return res
    return rec(n, memo)

t, l, r = map(int, input().split())
print((f(l) * t0 + f(l+1) * t1 + ... + f(r) * tr - l * f(r)) % mod)
