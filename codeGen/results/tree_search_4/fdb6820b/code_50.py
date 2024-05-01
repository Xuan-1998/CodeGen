from functools import lru_cache

@lru_cache(None)
def count_ways(i, j):
    if i == 0:
        return 1
    ways = 0
    for k in range(1, i+1):
        ways += count_ways(k-1, j-k)
    return ways

m, N = map(int, input().split())
dp = {}
for i in range(m+1):
    dp[i] = {}

print((sum(count_ways(i, N) for i in range(1, m+1)) % (10**9 + 7)) or 0)
