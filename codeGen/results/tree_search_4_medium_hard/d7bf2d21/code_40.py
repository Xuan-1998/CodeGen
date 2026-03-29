from collections import defaultdict

def findLengthOfLIS(nums):
    dp = [1] * len(nums)
    max_length = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    return sum(1 for x in dp if x == max_length)

nums = list(map(int, input().split()))
print(findLengthOfLIS(nums))
