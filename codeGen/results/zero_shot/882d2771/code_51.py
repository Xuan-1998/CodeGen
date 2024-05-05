import sys

t, l, r = map(int, input().split())

def f(n):
    return n - 1

expression = sum([t0 * (l + i - 1) for i in range(r-l+1)]) % (10**9 + 7)

print(expression)
