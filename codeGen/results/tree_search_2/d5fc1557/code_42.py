def longestSubarray(nums):
    n = len(nums)
    
    # Initialize dp table with zeros
    dp = [0] * (n + 1)
    
    # Base cases: When the array only contains 1's or starts with a 0
    if all(num == 1 for num in nums):
        return n
    
    # Transition from one state to another based on removing an element
    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        else: 
            dp[i] = max(dp[i - 1], dp[i - 2]) if i > 1 else 0
    
    # The maximum length of consecutive ones is the last element in dp table
    return dp[-1]
