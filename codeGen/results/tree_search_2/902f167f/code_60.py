def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: single unit square
    for j in range(m + 1):
        dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            dp[i][j] = min(dp[i-1][j], 1 + dp[1][j-i])

    return dp[n][m]

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_squares(n, m))
