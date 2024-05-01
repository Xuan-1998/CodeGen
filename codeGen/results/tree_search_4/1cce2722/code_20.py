from functools import lru_cache

@lru_cache(None)
def dp(i):
    if i < 0:
        return 0
    if i == 0:
        return a[0]
    if a[i] == a[i-1]:
        return dp(i-2) + 1
    else:
        return max(dp(i-1), dp(i-2))

n = int(input())
a = list(map(int, input().split()))
print(dp(n-1))
