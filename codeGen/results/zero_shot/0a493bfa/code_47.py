import sys
from functools import lru_cache

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

@lru_cache(None)
def f(s):
    p = next((p for p in range(2, int(s ** 0.5) + 1) if s % p == 0), None)
    if p is not None and p not in b:
        return f(s // p) + s
    else:
        return f(s // p) - s

def calc_beauty(a):
    beauty = 0
    for i in range(len(a)):
        if i > 0:
            a[i] = gcd(a[i], a[:i])
        beauty += f(a[i])
    return beauty

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

print(calc_beauty(a))
