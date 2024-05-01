def longest_ones_subarray(nums):
    n = len(nums)
    memo = {}

    def dp(i, ones):
        if (i, ones) in memo:
            return memo[(i, ones)]
        if i < 0 or ones <= 0:
            return 0

        if nums[i] == 1:
            result = dp(i - 1, ones + 1)
        else:
            if ones > 0:
                result = dp(i - 1, 0) + ones
            else:
                result = 0

        memo[(i, ones)] = result
        return result

    if n == 0 or all(num == 0 for num in nums):
        return 0

    return max(0, dp(n - 1, 0)) if all(num == 1 for num in nums[:n-1]) else dp(n - 1, 0)
