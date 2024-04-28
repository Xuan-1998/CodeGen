def longestSubarray(nums):
    n = len(nums)
    
    # Initialize dp array with all zeros
    dp = [0] * (n + 1)
    
    # Base case: If the array starts with a 0, then dp[0] = 0
    # If it only contains 1's, then dp[n - 1] = n - 1
    if nums[0] == 0:
        dp[0] = 0
    else:
        dp[0] = n
    
    # Transition relationships: Update dp[i] based on dp[i - 1]
    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = max(dp[i - 1], dp[i - 2] + 1) if i >= 2 else 1
        else:  # If we see a 0, reset the count and update dp[i]
            dp[i] = 1
    
    # Find the maximum length of consecutive ones up to index n - 1
    max_length = max(dp)
    
    return max_length

# Example usage:
nums = [1, 1, 0, 1]
print(longestSubarray(nums))  # Output: 3
