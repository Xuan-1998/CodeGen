def find_subset(nums):
    n = len(nums)
    m = 1000  # assuming m <= 1,000
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Base case: dp[0][j] = 1 if j == 0, and 0 otherwise.
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for k in range(m + 1):
            if nums[i - 1] <= k:
                # Include the number
                dp[i][k] = (dp[i - 1][k - nums[i - 1]] or 
                            dp[i - 1][k]) and True
            else:
                # Exclude the number
                dp[i][k] = dp[i - 1][k]
    
    return dp[n][m]
