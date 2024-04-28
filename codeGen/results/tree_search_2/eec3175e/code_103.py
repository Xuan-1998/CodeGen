def sum_divisible_by_m(n, m, numbers):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if numbers[i - 1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - numbers[i - 1]])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][m]

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

print(sum_divisible_by_m(n, m, numbers))
