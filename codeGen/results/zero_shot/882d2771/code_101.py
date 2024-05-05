import sys

t, l, r = map(int, input().split())

def f(n):
    res = 0
    while (1 << n) - 1 > 1:
        res += n
        n >>= 1
    return res + n

print(((sum(t * f(l+i) for i in range(r-l+1)) - l * f(r)) % (10**9+7)))
