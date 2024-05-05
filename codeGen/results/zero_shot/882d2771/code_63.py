import sys

t, l, r = map(int, input().split())
MOD = 10**9 + 7

# Simplified f(n) function
def f(n):
    return 2 * n - 1

result = sum(ti * f(li) for ti, li in zip(map(int, (0,) * t), range(l, r+1))) % MOD
print(result)
