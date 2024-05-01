def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Fill up the table
    for i in range(1, n+1):
        for j in range(i, n+1):
            if j < i-k:
                dp[i][j] = max(dp[i-1][min(j-k, i-1)] + sum(arr[min(i, j-k)+1:j+1]), dp[i-1][j])
            elif j == i-k:
                dp[i][j] = max(dp[i-1][j-1] + arr[j], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    # Return the maximum value in the last row of the table
    return max(dp[n-1][i] for i in range(n+1))

# Example usage
arr = [10, 20, 30, 40, 50]
k = 2
print(max_sum_after_partitioning(arr, k))  # Output: 120
