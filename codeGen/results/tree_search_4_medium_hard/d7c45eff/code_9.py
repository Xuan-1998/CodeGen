from functools import lru_cache

n, k = map(int, input().split())
s = input()

@lru_cache(None)
def dp(i, j):
    if i == 0 and j <= n:
        return ""
    elif j > i:
        return s[:i] + ("" if j > len(s) else "")
    else:
        return min((dp(i-1, j) + s[i-1]) if j > 1 or s[i-1] < dp(i-2, j-1)[j-1] else dp(i-2, j-1),
                   (dp(i-1, j-1) if i > 0 and (s[i-1] <= dp(i-2, j-2)[-1] or not s[i-1]) else "")
                   )

print(dp(n, k))
