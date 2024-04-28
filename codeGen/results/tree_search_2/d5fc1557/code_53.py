def findMaxConsecutiveOnes(nums):
    n = len(nums)
    dp = {0: 0}  # Initialize with base case
    max_length = 0
    
    for i in range(1, n):
        if nums[i] == 1:
            dp[i] = dp.get(i-1, 0) + 1  # Update the dynamic programming state
        else:
            dp[i] = max(dp.values())  # Reset to the maximum length of subarray ending at previous position
        max_length = max(max_length, dp[i])  # Keep track of the maximum length found so far
    
    return max_length
