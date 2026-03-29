import sys

t, l, r = map(int, sys.stdin.readline().split())
mod = 10**9 + 7

def f(n):
    return n - 1 + (n-2)//2

result = sum(t * f(i) for i in range(l, r+1)) - l * f(r)
print(result % mod)
