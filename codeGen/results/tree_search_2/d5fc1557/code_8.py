def longestSubarray(nums):
    n = len(nums)
    memo = {}

    def dp(i, ones):
        if (i, ones) in memo:
            return memo[(i, ones)]
        
        if i >= n or nums[i] == 0:
            return 0
        
        if ones > 0:
            result = max(ones + 1, dp(i-1, 0))
        else:
            result = max(dp(i-1, 0), 1)
        
        memo[(i, ones)] = result
        return result

    res = 0
    for i in range(n):
        res = max(res, dp(i, nums[i]))

    return res

# Example usage:
nums = list(map(int, input().split()))
print(longestSubarray(nums))
