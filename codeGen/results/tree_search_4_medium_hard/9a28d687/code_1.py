def min_cost(n):
    c = [int(input()) for _ in range(n)]
    s = [input() for _ in range(n)]

    dp = [[-1] * n for _ in range(n + 1)]

    def dfs(i, j):
        if dp[i][j] != -1:
            return dp[i][j]

        if i == 1:
            return c[j - 1]

        dp[i][j] = float('inf')
        for k in range(j):
            if s[k:j].join(s[:k]) <= s[0:i].join(s[i:]):
                dp[i][j] = min(dp[i][j], dfs(i - 1, k) + c[j - 1])
        return dp[i][j]

    return dfs(n, n)

print(min_cost(int(input())))
