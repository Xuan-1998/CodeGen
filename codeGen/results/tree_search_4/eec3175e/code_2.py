def subset_sum_divisible(n, m, arr):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    # Base case: dp[0][k] = 1 if k == 0, and 0 otherwise
    for j in range(m+1):
        dp[0][j] = 1 if j == 0 else 0
    
    # Fill the DP table
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = (dp[i-1][j] if j % m != 0 
                        or any((arr[k]%m == 0 and arr[k] <= j) 
                               for k in range(i)) 
                    else dp[i-1][j])
    
    return dp[n][m]
