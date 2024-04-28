def longestSubarray(nums):
    n = len(nums)
    memo = {}

    def dp(i, ones):
        if (i, ones) in memo:
            return memo[(i, ones)]
        if i == n:
            return 0
        if nums[i] == 1:
            result = dp(i + 1, ones + 1)
        else:
            result = 0
        for j in range(i - 1, -1, -1):
            if nums[j] == 0:
                break
            result = max(result, dp(j, 0) + i - j + 1)
        memo[(i, ones)] = result
        return result

    return dp(0, 0)

