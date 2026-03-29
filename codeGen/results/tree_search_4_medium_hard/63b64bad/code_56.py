    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    def dfs(x, y):
        if x <= 0 or x > n:
            return y
        if dp[x][y] != -1:
            return dp[x][y]
        res = max(dfs(x + a[x], y + a[x]), dfs(x + a[x] - 1, y))
        dp[x][y] = res
        return res

    for i in range(2, n + 1):
        print(dfs(i, 0))
