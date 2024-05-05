from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return ''
    if j == 0:
        return ''

    # If we delete the last character of s[:i], get dp[i-1][j-1]
    delete_last = dp(i - 1, j - 1)

    # If we duplicate s[:i-1] to get dp[i-1][j]
    duplicate = dp(i - 1, j)

    # Return the lexicographically smallest string
    return min(delete_last + s[i-1], duplicate + s[i-1]) if j > 0 else ''

k, n = map(int, input().split())
s = input()

print(min((dp(n, k), dp(n - 1, k)), key=lambda x: (x, len(x))))
