def isScrambled(s1, s2):
    n = len(s1)
    dp = [[[False] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    def dfs(i, j, k):
        if i == 0 and j == 0:
            return True
        if s1[i - 1] != s2[j - 1]:
            return False
        if dp[i][j][k]:
            return True
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            dp[i][j][k] = dfs(i - 1, j - 1, k) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1)
        else:
            for p in range(k):
                if (i > 0 and not dp[i - 1][j][p]) and (j > 0 and not dp[i][j - 1][p]):
                    dp[i][j][k] = dfs(i - 1, j, p) or dfs(i, j - 1, p)
        return dp[i][j][k]

    return dfs(n, n, 0)
