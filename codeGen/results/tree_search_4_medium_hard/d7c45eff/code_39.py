import sys
from functools import lru_cache

input()
n = int(input())
s = input().strip()

@lru_cache(None)
def dp(i, j):
    if i < 0:
        return ""
    if j < 0:
        return s[:i]
    if j == 0:
        return s[:i]
    
    if s[i] <= s[j]:
        return min(dp(i-1, j), s[i-1:i]+dp(i-1, j-1))
    else:
        return dp(i-1, j)

print(dp(n, k))
