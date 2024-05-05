def findLengthOfLIS(nums):
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

# Read input from stdin
nums = list(map(int, input().split()))

print(findLengthOfLIS(nums))
