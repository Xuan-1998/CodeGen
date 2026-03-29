import sys
mod = 10**9 + 7

def f(n):
    if n == 1:
        return 0  # base case: only one girl left, no comparisons needed
    else:
        return (2 * f(n // 2) + n % 2) % mod  # recursive formula

t, l, r = map(int, sys.stdin.readline().split())
result = t * f(l) - l * f(r)
print(result % mod)
