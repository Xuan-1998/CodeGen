def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 0
            elif i > 1 and j > 1:
                for k in range(min(i, j), 0, -1):
                    if (i % k) == 0 and (j % k) == 0:
                        dp[i][j] = min(dp[i][j], dp[i // k][j // k] + 1)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_squares(n, m))
