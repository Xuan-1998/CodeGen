from functools import lru_cache
n = int(input())
m = int(input())
a = input().strip()
b = input().strip()

@lru_cache(None)
def dp(i, j):
    if i == 0 or j == 0:
        return 0
    if a[i-1] != b[j-1]:
        return min(dp(i-1, j), dp(i, j-1))
    else:
        return dp(i-1, j-1) + 1

lcs = dp(n, m)
print(4*lcs - n-m)
