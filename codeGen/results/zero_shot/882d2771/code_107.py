import sys

def f(n):
    if n <= 2:
        return 1
    else:
        return 1 + min(f(k) for k in range(1, n//2+1)) + f(n-k-1)

t, l, r = map(int, input().split())
print((t0*f(l) + t1*f(l+1) + ... + tr - l*f(r)) % (10**9+7))
