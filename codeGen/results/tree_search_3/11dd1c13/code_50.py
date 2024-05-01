from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return 0
    min_sum = float('inf')
    for k in range(1, j+1):
        min_sum = min(min_sum, dp(i-1, k-1) * A[i][k]) + A[i][j]
    return min_sum

A = [list(map(int, input().split())) for _ in range(int(input()))]

print(dp(len(A), len(A[0])))
