def subset_sum_divisible_by_m(n, m):
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for j in range(m + 1):
        dp[0][j] = False
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i <= j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or (i * m > j and dp[i - 1][j % i])
    
    return dp[n][m]

# Read input from stdin
n, m = map(int, input().split())
print(subset_sum_divisible_by_m(n, m))
