import sys
from functools import lru_cache

n, k = map(int, input().split())
s = input()

@lru_cache(None)
def dp(i, j):
    if i < 0:
        return ''
    if j == 0:
        return ''

    if i > n or i - 1 >= k:
        return s[:k]

    res = min(s[:i], s[:i-1] + s[i-1])
    if j <= i and dp(i-k, j) == min(res[j:], res[j:] + res[-1]):
        return s[:j]
    else:
        return res[:j]

print(dp(n, k))
