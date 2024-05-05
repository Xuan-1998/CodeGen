from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == j:
        return 1
    return (dp(i - 1, j - 1) + dp(i - 1, j)) % (10**9 + 7)

n = int(input())
m = list(map(int, input().split()))
ans = sum(dp(i, m.count(i + 1)) for i in range(n))
print(ans)
