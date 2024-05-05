from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i, j):
    if i == 0 or j == 0:
        return ""
    if j <= n:
        return s[:i-1] + (s[i-1] if i > 0 else "")
    return dp(i, n) * (k - n)

n, k = map(int, input().split())
s = input()

result = dp(n, k)
print(result)
