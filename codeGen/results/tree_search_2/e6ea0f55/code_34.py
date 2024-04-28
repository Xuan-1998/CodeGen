def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k+1) for _ in range(n)]
    
    # Initialize the base case: if we have only one element, its sum is itself
    for j in range(k+1):
        dp[0][j] = nums[0]
        
    for i in range(1, n):
        for j in range(min(i, k)+1):
            # Consider all possible sums of subsequences with the last difference being j
            dp[i][j] = max(dp[i-1][k-j] + nums[i], dp[i-1][j])
            
    return max(dp[-1])

# Example usage:
nums = [10, 2, -3, 4, 5]
k = 3
print(maxSumSubsequence(nums, k))  # Output: 17

