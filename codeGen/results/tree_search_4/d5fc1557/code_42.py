from collections import defaultdict

def longest_subarray(nums):
    n = len(nums)
    dp = [False] * (n + 1)  # Initialize the dynamic programming table
    max_length = 0
    
    for i in range(n):
        if nums[i] == 1:
            dp[i + 1] = True
            max_length += 1
        else:
            max_length = 0
        
        dp[i + 1] = max_length > 0 and dp[i + 1]
    
    return max(i for i, val in enumerate(dp) if val) - 1

