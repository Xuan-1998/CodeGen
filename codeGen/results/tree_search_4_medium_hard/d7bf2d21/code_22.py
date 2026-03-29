def findLongestIncreasingSubsequence(nums):
    dp = {i: 1 for i in range(len(nums))}
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp.get(j, 0) + 1, dp.get(i, 0))
                
    return sum(1 for count in dp.values() if count == max(dp.values()))

# test the function
nums = [1,3,5,4,2]
print(findLongestIncreasingSubsequence(nums))  # Output: 2

