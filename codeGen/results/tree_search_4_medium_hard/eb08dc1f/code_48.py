def count_blocks(n):
    dp = [[0] * (n + 1) for _ in range(10)]
    MOD = 998244353

    def dfs(pos, last_digit):
        if pos > 10**n - 1:
            return 0
        if n == 0:
            return 1
        i = (pos // 10**n) % 10
        j = pos % 10
        if i == j and j == last_digit:
            return dp[9][j] * dfs(pos + 1, i)
        else:
            if i == j:
                dp[i][j] += dp[9][i]
            return (dp[i][j] + dfs(pos + 1, j)) % MOD

    result = [0] * (n + 1)
    for i in range(10):
        result[n - i] = dfs(i, i)
    print(*result, sep=' ')
