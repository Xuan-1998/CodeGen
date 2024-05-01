from functools import lru_cache

def isSubsetSumDivisibleByM(n, m):
    @lru_cache(None)
    def dfs(i, total):
        if total == 0:
            return True
        if i == 0 or total < 0:
            return False
        remainder = total % m
        if remainder == 0:
            return True
        return dfs(i-1, total) or dfs(i-1, total - S[i-1])

    S = [int(x) for x in input().split()]
    dp = [[False] * (m+1) for _ in range(n+1)]
    for i in range(m+1):
        dp[0][i] = True
    for i in range(1, n+1):
        for j in range(1, m+1):
            remainder = S[i-1] % m
            if remainder == 0:
                dp[i][j] = True
            else:
                dp[i][j] = dfs(i, j) or (i > 1 and dp[i-1][j-S[i-1]])
    return dp[n][m]
