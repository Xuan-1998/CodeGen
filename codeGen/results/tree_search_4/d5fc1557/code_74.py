codeblock

def longest_subarray(nums):
    n = len(nums)
    dp = [0] * n
    if nums[0] == 1:
        dp[0] = 1
    
    for i in range(1, n):
        if nums[i] == 1 and (i == 1 or nums[i-1] == 1):
            dp[i] = dp[i-1] + 1
        elif nums[i] == 0:
            dp[i] = max(dp[i-1], 1)
        else: #nums[i] == 0 and prev element was also 0
            dp[i] = dp[i-1]
    
    return max(dp)

