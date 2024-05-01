import sys
from functools import lru_cache

def min_squares(n, m):
    @lru_cache(None)
    def dp(i, j):
        if i == 0:
            return j // 2 + (j % 2)
        if j == 0:
            return i // 2 + (i % 2)
        
        ans = float('inf')
        for k in range(1, min(i, j) + 1):
            if i - k >= 0 and j - k >= 0:
                ans = min(ans, dp(i-k, j-k) + 1)
        
        return ans

    return dp(n, m)

n, m = map(int, input().split())
print(min_squares(n, m))
