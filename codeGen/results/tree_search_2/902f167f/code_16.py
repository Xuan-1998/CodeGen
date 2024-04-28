from functools import lru_cache

def min_squares(n, m):
    @lru_cache(None)
    def dp(i, j):
        if i == 1:
            return j
        if j == 1:
            return i
        if i > 1 and j > 1:
            return min(dp(i-1, j), dp(i, j-1)) + 1
        return max(i, j)

    return dp(n, m)


n, m = map(int, input().split())
print(min_squares(n, m))
