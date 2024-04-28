def can_sum_divisible_by_m(n, m, arr):
    dp = [[False for _ in range(m+1)] for _ in range(n+1)]
    
    # Initialize base cases
    for i in range(n+1):
        dp[i][0] = True
    
    # Fill up the dynamic programming table
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    # Check the last row of the table
    return dp[n][m]

# Example usage:
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_sum_divisible_by_m(n, m, arr))
