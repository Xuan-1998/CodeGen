def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if i <= c0:
            dp[i][0] = d0
        else:
            dp[i][0] = max(dp[i - 1][0], dp[c0][0])
    
    for j in range(1, m + 1):
        ai, bi, ci, di = map(int, input().split())
        
        for i in range(c0, n + 1):
            if i >= ci:
                dp[i][j] = max(dp[i - ci][j - 1] + di, dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j - 1]
    
    return dp[n][m]

print(solve())
