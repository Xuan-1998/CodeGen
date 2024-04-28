def dp(n, k):
    memo = [[0] * (k + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i > n or j == 0:
            return 1 if j == 0 else 0
        if memo[i][j] > 0:
            return memo[i][j]
        ans = 0
        for x in range(1, min(i + 1, j) + 1):
            if i % x == 0 and j >= x:
                ans += dfs(x - 1, j - x)
        memo[i][j] = ans % 1000000007
        return memo[i][j]

    return dfs(n, k)

# Read input from stdin
n, k = map(int, input().split())
print(dp(n, k))
