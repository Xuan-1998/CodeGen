from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 1 and j == 0:
        return 1
    if i == 0 or j == 0:
        return 0
    ans = sum(dp(i-1, k) for k in range(j+1)) % 1000000007
    return ans

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print((dp(N, M) - dp(0, M)) % 1000000007)
